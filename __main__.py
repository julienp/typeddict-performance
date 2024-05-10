from k8s_types import *

d: DeploymentArgsDict = {
    "metadata": {
        "name": "nginx",
    },
    "spec": {
        "selector":{
            "match_labels": {}
        },
        "replicas": 1,
        "template": {
            "metadata": {
                "labels": {}
            },
            "spec": {
                "containers": [{
                    "name": "nginx",
                    "image": "nginx"
                }]
            }
        }
    }
}

