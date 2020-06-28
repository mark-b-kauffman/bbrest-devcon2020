#!python3
# Mark Bykerk Kauffman
# Parses command line args and uses LinkContentCreator to create content with a link in an Ultra course
# Sample Use: 
# python use_content_creator.py --course_id "courseId:mbk-ultra" --link_url "https://www.blackboard.com" --title "Blackboard Title" --description "Blackboard Description"

import argparse
from config import ict
import datetime
from link_content_creator import LinkContentCreator
import time
import urllib3

def parse_argument():
    '''
    Argument definition and handling.
    '''
    parser = argparse.ArgumentParser(description='Create content at the root of an Ultra course that is a URL.')
    parser.add_argument('--course_id', dest='course_id', required=True, help='courseId where we create the content. courseId:<id>|uuid:<uuid>|pk1')
    parser.add_argument('--link_url', dest='link_url', required=True, help='The https link to the video.')
    parser.add_argument('--title', dest='title', required=True, help='Title for the content of the link.')
    parser.add_argument('--description', dest='description', required=True, help='Description for the link.')
   
    return parser.parse_args()


def main():
    '''
    Main method
    '''
    args = parse_argument()

    print("current date and time is..")
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)

    fqdn = ict['learn_rest_fqdn']
    key = ict['learn_rest_key']
    secret = ict['learn_rest_secret']

    link_creator = LinkContentCreator(fqdn, key, secret, args.course_id, args.link_url, args.title, args.description)
    link_creator.create_content_containing_link(args.course_id, "https://docs.blackboard.com", "Blackboard Dev Docs", "Read the Docs!" )

    print("current date and time is..")
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)

if __name__ == '__main__':
    main()
