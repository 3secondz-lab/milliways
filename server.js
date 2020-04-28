const YAML = require('yamljs');
const execSync = require('child_process').execSync;
const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:true}));

app.use('/nodeList', require('./dynamic_reconfigure_js/get_node_list'))

app.listen(3000, ()=>{console.log('server listen 3000')});