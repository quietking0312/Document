package main

import (
	"context"
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

type consumerHandler struct {
	Id string
}

func (consumerHandler) Setup(_ sarama.ConsumerGroupSession) error {
	return nil
}

func (consumerHandler) Cleanup(_ sarama.ConsumerGroupSession) error {
	return nil
}

func (c *consumerHandler) ConsumeClaim(session sarama.ConsumerGroupSession, claim sarama.ConsumerGroupClaim) error {
	for message := range claim.Messages() {
		fmt.Printf("consumId:%s, partition: %d, offeset: %d, key: %s, value: %s\n", c.Id, message.Partition, message.Offset, message.Key, message.Value)
		session.MarkMessage(message, "")
	}
	return nil
}

func Consumer() {
	consumerGroup, err := sarama.NewConsumerGroup([]string{"127.0.0.1:9092"}, "my_test_group", nil)
	if err != nil {
		fmt.Println("", err)
	}
	err = consumerGroup.Consume(context.Background(), []string{"my_test_topic"}, &consumerHandler{Id: "1"})
	if err != nil {
		fmt.Println("partition: ", err)
		return
	}
}

func Consumer2() {
	consumerGroup, err := sarama.NewConsumerGroup([]string{"127.0.0.1:9092"}, "my_test2_group", nil)
	if err != nil {
		fmt.Println("", err)
	}
	err = consumerGroup.Consume(context.Background(), []string{"my_test_topic"}, &consumerHandler{Id: "2"})
	if err != nil {
		fmt.Println("partition: ", err)
		return
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
	msg.Key = sarama.StringEncoder("hello")
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
	fmt.Printf("topics: %+v\n", topics["my_test_topic"])
	if err := admin.CreateTopic("my_test_topic", &sarama.TopicDetail{NumPartitions: 3, ReplicationFactor: 1}, false); err != nil {
		fmt.Println(err)
		return
	}
	//if err := admin.CreateTopic("my_test_topic", &sarama.TopicDetail{NumPartitions: 1, ReplicationFactor: 1}, false); err != nil {
	//	fmt.Println("newTopic, ", err)
	//	return
	//}
	//topics, err = admin.ListTopics()
	//if err != nil {
	//	fmt.Println("listTopics: ", err)
	//	return
	//}
	//fmt.Println(topics)
	go Consumer()
	go Consumer2()
	for i := 0; i < 1; i++ {
		Producer(config, msg)
	}
	time.Sleep(30 * time.Second)
}
