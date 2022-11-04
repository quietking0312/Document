package main

import "strings"

type MYMIME map[string]string

func (m MYMIME) GetMime(path string) string {
	for k, v := range m {
		sList := strings.Split(k, " ")
		for _, key := range sList {
			if strings.HasSuffix(path, key) {
				return v
			}
		}
	}
	return "application/octet-stream"
}

var DefaultMime = MYMIME{
	"js.gz":                          "application/javascript",
	"wasm.gz":                        "application/wasm",
	"data.gz symbols.json.gz glb.gz": "text/plain",

	"html htm shtml": "text/html",
	"css":            "text/css",
	"xml":            "text/xml",
	"gif":            "image/gif",
	"jpeg jpg":       "image/jpeg",
	"js":             "application/javascript",
	"atom":           "application/atom+xml",
	"rss":            "application/rss+xml",
	"mml":            "text/mathml",
	"txt":            "text/plain",
	"jad":            "text/vnd.sun.j2me.app-descriptor",
	"wml":            "text/vnd.wap.wml",
	"htc":            "text/x-component",
	"png":            "image/png",
	"tif tiff":       "image/tiff",
	"wbmp":           "image/vnd.wap.wbmp",
	"ico":            "image/x-icon",
	"jng":            "image/x-jng",
	"bmp":            "image/x-ms-bmp",
	"svg svgz":       "image/svg+xml",
	"webp":           "image/webp",
	"woff":           "application/font-woff",
	"jar war ear":    "application/java-archive",
	"json":           "application/json",
	"hqx":            "application/mac-binhex40",
	"doc":            "application/msword",
	"pdf":            "application/pdf",
	"ps eps ai":      "application/postscript",
	"rtf":            "application/rtf",
	"m3u8":           "application/vnd.apple.mpegurl",
	"xls":            "application/vnd.ms-excel",
	"eot":            "application/vnd.ms-fontobject",
	"ppt":            "application/vnd.ms-powerpoint",
	"wmlc":           "application/vnd.wap.wmlc",
	"kml":            "application/vnd.google-earth.kml+xml",
	"kmz":            "application/vnd.google-earth.kmz",
	"7z":             "application/x-7z-compressed",
	"cco":            "application/x-cocoa",
	"jardiff":        "application/x-java-archive-diff",
	"jnlp":           "application/x-java-jnlp-file",
	"run":            "application/x-makeself",
	"pl pm":          "application/x-perl",
	"prc pdb":        "application/x-pilot",
	"rar":            "application/x-rar-compressed",
	"rpm":            "application/x-redhat-package-manager",
	"sea":            "application/x-sea",
	"swf":            "application/x-shockwave-flash",
	"sit":            "application/x-stuffit",
	"tcl tk":         "application/x-tcl",
	"der pem crt":    "application/x-x509-ca-cert",
	"xpi":            "application/x-xpinstall",
	"xhtml":          "application/xhtml+xml",
	"xspf":           "application/xspf+xml",
	"zip":            "application/zip",
	"bin exe dll":    "application/octet-stream",
	"deb":            "application/octet-stream",
	"dmg":            "application/octet-stream",
	"iso img":        "application/octet-stream",
	"msi msp msm":    "application/octet-stream",
	"docx":           "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
	"xlsx":           "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
	"mp4":            "video/mp4",
	"mpeg mpg":       "video/mpeg",
	"mov":            "video/quicktime",
	"webm":           "video/webm",
	"flv":            "video/x-flv",
	"m4v":            "video/x-m4v",
	"mng":            "video/x-mng",
	"asx asf":        "video/x-ms-asf",
	"wmv":            "video/x-ms-wmv",
	"avi":            "video/x-msvideo",
}
