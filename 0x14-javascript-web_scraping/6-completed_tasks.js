#!/usr/bin/node
// request is used to compute the number of tasks completed by user
const request = require('request');
const APIurl = process.argv[2];

request(APIurl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const tasks = JSON.parse(body);
  const taskDONE = {};

  tasks.forEach(task => {
    if (task.completed) {
      if (taskDONE[task.userID]) {
        taskDONE[task.userID]++;
      } else {
        taskDONE[task.userID] = 1;
      }
    }
  });

  console.log(taskDONE);
});
