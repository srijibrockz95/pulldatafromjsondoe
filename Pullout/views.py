"""
Routes and views for the flask application.
"""
import json
import base64
from io import BytesIO
import numpy as np 
import matplotlib.pyplot as plt
from flask import *
from Pullout import app, db
from Pullout.models import Jenkinsmonitordata

jmonitor = Blueprint('employee', __name__)

cols = ['DisplayName', 'NextBuildNumber', 'HealthReport', 'LastSuccessfulBuild', 'LastFailedBuild']

@jmonitor.route('/showdataintable', methods=['GET'])
def showdataintable():
    try:
        if request.method == 'GET':
            with open("./Pullout/data.json") as f:
                jdata = json.load(f)
                if "displayName" in jdata:
                    dname = jdata["displayName"]
                if "healthReport" in jdata:
                    hreport = jdata["healthReport"][0]["score"]
                if "nextBuildNumber" in jdata:
                    noofbuilds = jdata["nextBuildNumber"]
                if "lastSuccessfulBuild" in jdata:
                    lsbuild = jdata["lastSuccessfulBuild"]["number"]
                if "lastFailedBuild" in jdata:
                    lfailedbuild = jdata["lastFailedBuild"]["number"]
            existing_jobname = Jenkinsmonitordata.query.filter(Jenkinsmonitordata.DisplayName == dname).one_or_none()
            if existing_jobname is None:
                jmd = Jenkinsmonitordata(DisplayName=dname, NextBuildNumber=noofbuilds, HealthReport=hreport, LastSuccessfulBuild=lsbuild, LastFailedBuild=lfailedbuild)
                db.session.add(jmd)
                db.session.commit()
                readjmd = Jenkinsmonitordata.query.all()
                result = [{col: getattr(d, col) for col in cols} for d in readjmd]
                return render_template("showdataintable.html", jobname=result[0]["DisplayName"], noofbuilds=result[0]["NextBuildNumber"], healthreport=result[0]["HealthReport"], lastfailedbuilds=result[0]["LastFailedBuild"], lastsuccessbuilds=result[0]["LastSuccessfulBuild"])
            else:
                return jsonify({"message": "Job {dname} already exists."})
    except Exception as e:
        return e

@jmonitor.route('/showdataingraph', methods=['GET'])
def showdataingraph():
    readjmd = Jenkinsmonitordata.query.all()
    result = [{col: getattr(d, col) for col in cols} for d in readjmd]
    title=result[0]["DisplayName"]
    del result[0]["DisplayName"]
    xdata = list(result[0].keys())
    ydata = list(result[0].values())

    fig = plt.figure(figsize = (8, 4)) 
  
    plt.bar(xdata, ydata, color ='black',  
        width = 0.2) 
  
    plt.xlabel("Parameters") 
    plt.ylabel("Limit") 
    plt.title("Job name: "+title)
    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    return render_template("showdataingraph.html", plottedgraph=encoded)

@jmonitor.route("/hello")
def hello():
     return 'Hello Srijib, Welcome to AWS!'
