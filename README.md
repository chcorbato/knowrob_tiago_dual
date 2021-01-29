
# knowrob_tiago_dual
This repository contains a simple exame of a KnowRob 2.0 package that defines a simple ontology for a retail scenario at AIRLab Delft and a ROS node to control a [simulation of the AIRLab tiago robot](https://gitlab.tudelft.nl/cor/ro47014/retail_store_lightweight_sim). It uses KnowRob to perform queries on the ontology and drive a simple sense-act control loop for a pick and place task.

**Note**:This repository is based on the example: https://github.com/ipa-hsd/knowrob_moveit

# Installation  
Follow `KnowRob` installation steps: https://github.com/knowrob/knowrob to install KnowRob in your ROS workspace.

### Install robot simulation
Follow the instructions at https://gitlab.tudelft.nl/cor/ro47014/retail_store_lightweight_sim to install the simulation in your ROS workspace.

#### Clone `knowrob_tiago_dual` package in your workspace
```
cd <path/to/workspace/src>
git clone https://github.com/chcorbato/knowrob_tiago_dual
cd ..
source /opt/ros/melodic/setup.bash 
catkin b
source devel/setup.bash and build again
```

# Usage
```
# Terminal 1
sudo systemctl start mongod.service
roslaunch knowrob knowrob.launch

# Terminal 2
$ rosrun knowrob_tiago_dual knowrob_tiago_dual
```

## Debugging database and reasoning
A convenient method to debug what is going on in the KnowRob DB is to use [`rosprolog_commandline`](https://github.com/knowrob/rosprolog/blob/527e791b917490357bdfb7421becf66984a4cece/README.md#rosprolog-node-console)

```
rosrun rosprolog rosprolog_commandline.py
```