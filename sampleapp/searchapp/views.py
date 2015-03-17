import os
import csv
import json

from django.shortcuts import render
from httplib import HTTPResponse
from models import MPattendence

# Create your views here.
def home(request):
    mp_data = MPattendence.objects.all()
    return render(request, 'base.html', {"mp_data": mp_data})


def load_csv_data(request):
    filepath = "/home/hasher/workspace/workspace1/WebApp/sampleapp/searchapp/datafile.csv"
    csv_data = read_csv_data(filepath)
    for data in csv_data:
        if csv_data.index(data)!=0:
            mp_attendence_obj = MPattendence(division_or_seat_num=int(data['division_or_seat_num']),
                            member_name=data['member_name'].strip(), lok_sabha = int(data['lok_sabha']),
                            session=int(data['session']), state=data['state'], constituency=data['constituency'],
                            total_seats=int(data['total_seats']), num_of_days=0)
            mp_attendence_obj.save()
    return HTTPResponse("Successfull uploaded csv data.")

def read_csv_data(filepath):
    fieldnames = ("S.No", "division_or_seat_num", "member_name", "lok_sabha",
                  "session", "state", "constituency", "total_seats", "num_of_days")
    try:
        csvfile = open(filepath, 'r')
    except:
        raise "Not able to read the csv file."
    reader = csv.DictReader(csvfile, fieldnames)
    csv_data = []
    for row in reader:
        csv_data.append(row)
    return csv_data
