#!/usr/bin/node
// fs and  request are used to get the content of a webpage and the stores it in a file
const fs = require('fs')
const request = require('request')

const webpageURL = process.argv[2]
const fileName = process.argv[3]

request(webpageURL, (error, response, body) => {
  if (error) {
    console.error(error)
    return
  }

  fs.writeFile(fileName, body, 'utf8', (err) => {
    if (err) {
      console.error(err)
      return
    }
  })
})
