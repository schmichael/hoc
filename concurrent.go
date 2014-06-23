package main

import "net/http"

func main() {
	go http.Get("http://google.com/?q=independent")
	go http.Get("http://google.com/?q=tasks")
}
