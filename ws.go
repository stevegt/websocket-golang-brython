package main

import (
	// "fmt"
	"github.com/gorilla/websocket"
	// "io/ioutil"
	"log"
	"net/http"
)

func main() {
	// http.HandleFunc("/ws", wsHandler)
	http.HandleFunc("/ws", echo)
	http.Handle("/", http.FileServer(http.Dir("./static")))
	// http.HandleFunc("/", rootHandler)

	panic(http.ListenAndServe(":8080", nil))
}

var upgrader = websocket.Upgrader{
	CheckOrigin: func(r *http.Request) bool {
		return true
	},
}

func echo(w http.ResponseWriter, r *http.Request) {
	c, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		log.Print("upgrade:", err)
		return
	}
	defer c.Close()
	for {
		mt, message, err := c.ReadMessage()
		if err != nil {
			log.Println("read:", err)
			break
		}
		log.Printf("recv: %s", message)
		// message = []byte(fmt.Sprintf("got %s", message))
		err = c.WriteMessage(mt, message)
		if err != nil {
			log.Println("write:", err)
			break
		}
	}
}
