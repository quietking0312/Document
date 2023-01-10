package main

import (
	"context"
	"errors"
	"fmt"
	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/credentials"
	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
	"github.com/aws/aws-sdk-go-v2/service/s3"
	"github.com/aws/aws-sdk-go-v2/service/s3/types"
	"github.com/spf13/cobra"
	"log"
	"os"
	"path"
	"strings"
	"sync"
	"time"
)

var version string
var buildTime string
var awsKey string
var awsSecret string

func FileForEach(dirPath string) []string {
	files, err := os.ReadDir(dirPath)
	if err != nil {
		log.Fatalln(err)
	}
	var myFile []string
	for _, file := range files {
		filePath := path.Join(dirPath, file.Name())
		if file.IsDir() {
			subFile := FileForEach(filePath)
			if len(subFile) > 0 {
				myFile = append(myFile, subFile...)
			}
		} else {
			myFile = append(myFile, filePath)
		}
	}
	return myFile
}

func UploadFile(uploader *manager.Uploader, bucket, localFilePath, remoteFilePath string) bool {
	data, err := os.Open(localFilePath)
	if err != nil {
		log.Fatalln(err)
	}
	defer data.Close()
	ctx := context.Background()
	opts := &s3.PutObjectInput{
		Bucket:      aws.String(bucket),
		Key:         aws.String(remoteFilePath),
		Body:        data,
		ACL:         types.ObjectCannedACLPublicRead,
		ContentType: aws.String(DefaultMime.GetMime(remoteFilePath)),
	}
	if strings.HasSuffix(remoteFilePath, "gz") {
		opts.ContentEncoding = aws.String("gzip")
	}
	result, err := uploader.Upload(ctx, opts)
	if err != nil {
		var mu manager.MultiUploadFailure
		if errors.As(err, &mu) {
			fmt.Println(err)
			_ = mu.UploadID()
			return false
		} else {
			fmt.Println(err)
			return false
		}
	}
	fmt.Println("", result.Location)
	return true
}

type ErrFileItem struct {
	RemotePath string
	LocalPath  string
}

func main() {
	var showVersion bool
	var bucket string
	var localPath string
	var remotePath string
	var region string
	//var mode string
	//localPath = "D:\\Desktop\\live_AT1"
	var rootCmd = &cobra.Command{
		Use:   "root",
		Short: "",
		Run: func(cmd *cobra.Command, args []string) {
			if showVersion {
				fmt.Printf("UTC build time: %s\n", buildTime)
				fmt.Printf("Build from version: %s\n", version)
				return
			}

			fileList := FileForEach(localPath)
			if len(fileList) < 0 {
				return
			}

			conf, err := config.LoadDefaultConfig(context.TODO(),
				config.WithCredentialsProvider(credentials.NewStaticCredentialsProvider(awsKey, awsSecret, "")))
			if err != nil {
				log.Fatalf("%v\n", err)
			}
			cli := s3.NewFromConfig(conf, func(options *s3.Options) {
				options.Region = region
			})
			uploader := manager.NewUploader(cli)
			var errFiles []ErrFileItem
			var group sync.WaitGroup
			t := time.Now().Unix()
			num := len(fileList)
			fmt.Printf("开始上传, 共%d个文件\n", num)
			for _, localFilePath := range fileList {
				remoteFilePath := strings.Replace(localFilePath, path.Join(localPath), "", 1)
				remoteFilePath = strings.Trim(remoteFilePath, "/")
				remoteFilePath = strings.Trim(remoteFilePath, "\\")
				remoteFilePath = strings.Replace(remoteFilePath, "\\", "/", -1)
				if remotePath != "" {
					remoteFilePath = path.Join(remotePath, remoteFilePath)
				}
				group.Add(1)
				go func(localFilePath, remoteFilePath string) {
					defer group.Done()
					if !UploadFile(uploader, bucket, localFilePath, remoteFilePath) {
						errFiles = append(errFiles, ErrFileItem{
							RemotePath: remoteFilePath,
							LocalPath:  localFilePath,
						})
					}
				}(localFilePath, remoteFilePath)
			}
			group.Wait()
			var err2Files []ErrFileItem
			if len(errFiles) > 0 {
				fmt.Printf("上传完成，共%d个文件, 成功%d个文件, 失败%d个文件, 开始重试\n", num, num-len(errFiles), len(errFiles))
				for _, item := range errFiles {
					if !UploadFile(uploader, bucket, item.LocalPath, item.RemotePath) {
						err2Files = append(err2Files, item)
					}
				}
			}
			len2 := len(err2Files)
			netT := time.Now().Unix()
			fmt.Printf("上传完成：用时%d秒, 共%d个文件 成功%d个文件, 失败%d个文件\n", netT-t, num, num-len2, len2)
			if len2 > 0 {
				fmt.Println("开始打印失败文件")
				for _, item := range err2Files {
					fmt.Println(item.RemotePath)
				}
			}
		},
	}
	rootCmd.Flags().BoolVarP(&showVersion, "version", "v", false, "显示版本号")
	rootCmd.Flags().StringVarP(&bucket, "bucket", "b", "release-byte-city", "储存桶名称")
	rootCmd.Flags().StringVarP(&region, "region", "r", "us-east-1", "地区")
	rootCmd.Flags().StringVarP(&localPath, "localPath", "l", "", "上传本地目录")
	rootCmd.Flags().StringVarP(&remotePath, "remotePath", "p", "", "远程目录")
	//rootCmd.Flags().StringVarP(&mode, "mode", "m", "dir", "模式 [dir]")
	if err := rootCmd.Execute(); err != nil {
		os.Exit(1)
	}
}
