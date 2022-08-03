package main

import (
	"fmt"
	"github.com/Shopify/sarama"
	"time"
)

func Producer(config *sarama.Config, msg *sarama.ProducerMessage) {
	client, err := sarama.NewSyncProducer([]string{"127.0.0.1:9092"}, config)
	if err != nil {
		fmt.Println("producer close err, ", err)
		return
	}
	defer client.Close()
	pid, offset, err := client.SendMessage(msg)
	if err != nil {
		fmt.Println("send message failed, ", err)
		return
	}
	fmt.Printf("id：%v, offset:%v \n", pid, offset)
}

func Consumer() {
	consumer, err := sarama.NewConsumer([]string{"127.0.0.1:9092"}, nil)
	if err != nil {
		fmt.Println("newConsumer: ", err)
		return
	}
	defer consumer.Close()
	partitionList, err := consumer.Partitions("my_test_topic")
	if err != nil {
		fmt.Println("partition: ", err)
		return
	}
	fmt.Println(partitionList)
	for _, partition := range partitionList {
		fmt.Println(partition)
		pc, err := consumer.ConsumePartition("my_test_topic", partition, sarama.OffsetNewest)
		if err != nil {
			fmt.Println(err)
			return
		}
		for m := range pc.Messages() {
			fmt.Printf("partition: %d, offeset: %d, key: %s, value: %s\n", m.Partition, m.Offset, m.Key, m.Value)
		}
	}
}

func main() {
	config := sarama.NewConfig()
	config.Producer.RequiredAcks = sarama.WaitForAll
	config.Producer.Partitioner = sarama.NewRandomPartitioner
	config.Version = sarama.V2_1_0_0
	config.Producer.Return.Successes = true
	msg := &sarama.ProducerMessage{}
	msg.Topic = "my_test_topic"
	msg.Value = sarama.StringEncoder("this is test")
	admin, err := sarama.NewClusterAdmin([]string{"127.0.0.1:9092"}, config)
	if err != nil {
		fmt.Println("admin, ", err)
		return
	}
	defer admin.Close()
	topics, err := admin.ListTopics()
	if err != nil {
		fmt.Println("listTopics: ", err)
		return
	}
	fmt.Println(topics)
	if err := admin.CreateTopic("sss", &sarama.TopicDetail{NumPartitions: 1, ReplicationFactor: 1}, false); err != nil {
		fmt.Println("newTopic, ", err)
		return
	}
	topics, err = admin.ListTopics()
	if err != nil {
		fmt.Println("listTopics: ", err)
		return
	}
	fmt.Println(topics)
	go Consumer()
	for i := 0; i < 10; i++ {
		Producer(config, msg)
	}
	time.Sleep(30 * time.Second)
}
