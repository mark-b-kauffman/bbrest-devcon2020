#!python3
# File: link_content_creator.py
# Author: Mark Bykerk Kauffman
# Class LinkContentCreator - to create content that contains a link.
# Input: 
#   Ultra Learn FQDN, REST Key, Secret, Course ID of an Ultra Course, Video content URL, Description text
from bbrest import BbRest
import os
import requests
import codecs
import time
from datetime import datetime
import copy

class LinkContentCreator:
    def __init__(self, learnfqdn, key, secret, course_id, link_url, title, description):
        '''
        Constructor of uploader instance. 
        This goes through authorization step of the target server.
        '''
        self.learnfqdn = learnfqdn
        self.key = key
        self.secret = secret
        self.course_id = course_id # represents the courseId could be "_2_7", or "uuid:<a_uuid>" or "courseId:mbk-ultra"
        self.link_url = link_url
        self.title = title
        self.description = description

        self.bb = BbRest(key, secret, f"https://{learnfqdn}")

        self.the_payload =  {   'title': f"{title}",
                                'description': f"{description}",
                                'body': "contentBody",
                                'position': 0,
                                'contentHandler': {
                                'id': 'resource/x-bb-externallink',
                                'url': f"{link_url}"
                                },
                                'availability': {
                                'available': 'Yes',
                                }
                            }

    def get_system_version(self):
        '''
        Test method that just makes REST call to /learn/api/public/v1/system/version
        '''
        resp = self.bb.GetSystemVersion()
        return resp

    def create_content(self): # Use the values given when instantiating this.
        resp = self.bb.CreateChild(courseId=f'{self.course_id}', contentId='root', payload=self.the_payload)
        return resp

    
    def create_content_containing_link(self, course, link_url, title, description): #Python can't overload method signatures.
        new_payload =  {   'title': f"{title}",
                                'description': f"{description}",
                                'body': "contentBody",
                                'position': 0,
                                'contentHandler': {
                                'id': 'resource/x-bb-externallink',
                                'url': f"{link_url}"
                                },
                                'availability': {
                                'available': 'Yes',
                                }
                            }
        resp = self.bb.CreateChild(courseId=f'{self.course_id}', contentId='root', payload=new_payload)
        print (resp.json())
        return resp
