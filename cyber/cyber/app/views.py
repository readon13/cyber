from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
import logging
import json
import string
import sys
import requests
import datetime
import os
import base64
import datetime
import redis
import time
import re
import redis
# importing the threading module
import threading

from cyber.app.owsapzap import zap_scan

from cyber.app.ingest import createReport

from cyber.app.ingest import ingest_wapiti, ingest_nikto, ingest_owasp_zap, ingest_nmap


def nmap(url,reportid):
    str1 = url
    str2 = reportid
    print(str1)
    # print ('nmap -sV -oN '+os.getcwd()+'/report/'+str2+'_nmap.text '+str1)
    os.chdir(os.getcwd() + '/cyber/app/report')
    os.system('nmap -sV -oN ' + str2 + '_nmap.text ' + str1)
    #insertDb
    ingest_nmap(reportid)


def nikto(url,reportid):
    str1 = url
    str2 = reportid
    print(str1)
    os.chdir(os.getcwd() + '/cyber/app/report')
    os.system('/Users/856521/PycharmProjects/suman/nikto/program/nikto.pl -h ' + str1 + ' -output ' + str2 + '_nikto.html')
    #insertDb
    ingest_nikto(reportid)



def owsapzap(url,reportid):
    str1 = url
    str2 = reportid
    print(str1)
    zap_scan(str1, str2)
    #insertDb
    ingest_owasp_zap(reportid)


def wapiti(url,reportid):
    str1 = url
    str2 = reportid
    print(str1)
    path = os.getcwd() + '/cyber/app/report'
    os.system(
        'wapiti -u ' + str1 + ' -f html -o ' + path)


    #insertDb
    ingest_wapiti(reportid)


@api_view(['GET', 'POST'])
def trigger_scan(request):
    """
    List all code snippets, or create a new snippet.
    """
    content = {'please move along': 'nothing to see here'}
    if request.method == 'GET':
        return Response(content)

    elif request.method == 'POST':
        print(request.data)
        print(request)
        data1 = json.dumps(request.data)
        data2 = json.loads(data1)
        str1=data2['url']
        str2 = data2['userid']
        print(str2)
        responseData="Measurement of NO added now"
        #Capturing report Id
        str2 = createReport(str2)


        t1 = threading.Thread(target=nmap, args=(str1,str2))
        t2 = threading.Thread(target=nikto, args=(str1,str2))
        t3 = threading.Thread(target=owsapzap, args=(str1,str2))
        t4 = threading.Thread(target=wapiti, args=(str1,str2))

        t1.start()
        t2.start()
        t3.start()
        t4.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()

        return Response(responseData, status=status.HTTP_200_OK)
        return Response(content, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def nmap_scan(request):
    """
    List all code snippets, or create a new snippet.
    """
    content = {'please move along': 'nothing to see here'}
    if request.method == 'GET':
        return Response(content)

    elif request.method == 'POST':
        print(request.data)
        print(request)
        data1 = json.dumps(request.data)
        data2 = json.loads(data1)
        str1=data2['url']
        str2 = data2['reportid']
        print(str1)
        #print ('nmap -sV -oN '+os.getcwd()+'/report/'+str2+'_nmap.text '+str1)
        os.chdir(os.getcwd()+'/cyber/app/report')
        os.system('nmap -sV -oN '+str2+'_nmap.text '+str1)


        responseData="Measurement of NO added now"
        return Response(responseData, status=status.HTTP_200_OK)
        return Response(content, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def nikto_scan(request):
    """
    List all code snippets, or create a new snippet.
    """
    content = {'please move along': 'nothing to see here'}
    if request.method == 'GET':
        return Response(content)

    elif request.method == 'POST':
        print(request.data)
        print(request)
        data1 = json.dumps(request.data)
        data2 = json.loads(data1)
        str1 = data2['url']
        str2 = data2['reportid']
        print(str1)
        os.chdir(os.getcwd() + '/cyber/app/report')
        os.system('/Users/856521/PycharmProjects/suman/nikto/program/nikto.pl -h '+str1+' -output '+str2+'_nikto.html')

        responseData = "Measurement of NO added now"
        return Response(responseData, status=status.HTTP_200_OK)
        return Response(content, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def owsapzap_scan(request):
    """
    List all code snippets, or create a new snippet.
    """
    content = {'please move along': 'nothing to see here'}
    if request.method == 'GET':
        return Response(content)

    elif request.method == 'POST':
        print(request.data)
        print(request)
        data1 = json.dumps(request.data)
        data2 = json.loads(data1)
        str1 = data2['url']
        str2 = data2['reportid']
        print(str1)
        zap_scan(str1, str2)

        responseData = "Measurement of NO added now"
        return Response(responseData, status=status.HTTP_200_OK)
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def wapiti_scan(request):
    """
    List all code snippets, or create a new snippet.
    """
    content = {'please move along': 'nothing to see here'}
    if request.method == 'GET':
        return Response(content)

    elif request.method == 'POST':
        print(request.data)
        print(request)
        data1 = json.dumps(request.data)
        data2 = json.loads(data1)
        str1 = data2['url']
        str2 = data2['reportid']
        print(str1)
        path = os.getcwd() + '/cyber/app/report'
        os.system(
            'wapiti -u '+str1+' -f html -o '+path)

        responseData = "Measurement of NO added now"
        return Response(responseData, status=status.HTTP_200_OK)
        return Response(content, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def trigger_scan(request):
    """
    List all code snippets, or create a new snippet.
    """
    content = {'please move along': 'nothing to see here'}
    if request.method == 'GET':
        return Response(content)

    elif request.method == 'POST':
        print(request.data)
        print(request)
        data1 = json.dumps(request.data)
        data2 = json.loads(data1)
        str1=data2['url']
        print(str1)
        responseData="Measurement of NO added now"
        return Response(responseData, status=status.HTTP_200_OK)
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

