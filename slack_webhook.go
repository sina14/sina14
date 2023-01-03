package main

import (
	"fmt"

	"github.com/slack-go/slack"
)

func main() {
	api := slack.New("YOUR_TOKEN_HERE")
	channelID, timestamp, err := api.PostMessage("#mychannel", slack.MsgOptionText("Hello, World!", false))
	if err != nil {
		fmt.Printf("%s\n", err)
		return
	}
	fmt.Printf("Message successfully sent to channel %s at %s", channelID, timestamp)
}
