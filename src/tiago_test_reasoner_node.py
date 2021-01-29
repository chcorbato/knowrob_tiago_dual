#!/usr/bin/env python

# Author: c.h.corbato@tudelft.nl

import rospy
import os

import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import geometry_msgs.msg

import roslib; roslib.load_manifest("rosprolog")
from rosprolog_client import * # PrologException, Prolog

if __name__ == "__main__":
    try:
        rospy.init_node("tiago_test_reasoner")
        rospy.spin()
        prolog = Prolog()  # start communication with rosprolog

        # create skill clients
        # move_base_client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
        # rospy.loginfo('Waiting for servers...')
        # move_base_client.wait_for_server()

        # navigate to goal_pose = shelf
        # pose_goal = geometry_msgs.msg.Pose()
        # pose_goal.position.x = -0.40
        # pose_goal.position.y = 0.0
        # pose_goal.orientation.z = 1.0
        # pose_goal.orientation.w = 0.0
        # goal = MoveBaseGoal()
        # goal.target_pose.header.frame_id = "map"
        # goal.target_pose.header.stamp = rospy.Time.now()
        # goal.target_pose.pose = pose_goal
        # rospy.loginfo('Sending move base goal...')
        # move_base_client.send_goal(goal)
        # move_base_client.wait_for_result()
        # rospy.loginfo('Navigation finished')

        query = prolog.query("register_ros_package(knowrob_tiago_dual)") # uncomment to register package
        prolog.query('tripledb_forget(_,_,_).') # clean DB before starting
        
        # make queries
        query = prolog.query("triple(R, 'http://www.w3.org/2002/07/owl#onProperty', 'http://knowrob.org/kb/srdl2-cap.owl#hasCapability'), \
                   triple(R, 'http://www.w3.org/2002/07/owl#someValuesFrom', Cap), \
                   subclass_of(Cap, Desc), \
                   triple(Desc, 'http://www.w3.org/2002/07/owl#onProperty', 'http://knowrob.org/kb/srdl2-comp.owl#dependsOnComponent'), \
                   triple(Desc, 'http://www.w3.org/2002/07/owl#someValuesFrom', Comp), \
                   triple(CompInst, 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type', Comp)")

        for solution in query.solutions():
            print("Robot: "+ solution["R"])
            print("Capability: "+solution["Cap"])
            print("Component: "+solution["Comp"])


    except rospy.ROSInterruptException:
        pass