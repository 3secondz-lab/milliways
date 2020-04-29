/*
    ROS Javascript dynamic_reconfigure simple example
    Jinsun Park
    (zzangjinsun@3secondz.com)
*/

// HOW TO USE :
// $ node get_node_list.js

// Import modules
const YAML = require('yamljs');
const execSync = require('child_process').execSync;

// Get list of reconfigurable nodes
var list_nodes = execSync("rosrun dynamic_reconfigure dynparam list", { shell: "/bin/bash" }).toString();
list_nodes = list_nodes.split('\n');

for(var i = 0; i < list_nodes.length; i++){
    var name_node = list_nodes[i];

    if(name_node == ''){
        continue;
    }

    // Get reconfigurable parameters
    var list_vars = execSync("rosrun dynamic_reconfigure dynparam get " + name_node).toString();

    // Parse using YAML
    list_vars = YAML.parse(list_vars);

    // Get keys
    var list_keys = Object.keys(list_vars);
    var list_types = []

    // Get types of keys
    for(var j = 0; j < list_keys.length; j++){
        list_types.push(typeof(list_vars[list_keys[j]]))
    }

    // Log
    console.log('Node : ' + name_node)
    for(var j = 0; j < list_keys.length; j++){
        // Ignore groups
        if(list_keys[j] == 'groups'){
            continue;
        }
        console.log(list_keys[j] + ' (' + list_types[j] + ') : ' + list_vars[list_keys[j]])
    }
    console.log('\n')
}
