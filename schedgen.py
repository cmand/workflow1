#!/usr/bin/env python3

import time
import sys
import os
from datetime import date, timedelta, datetime

flair = {
  'odd':'<tr class="odd">',
  'even':'<tr>',
  'quiz':'<tr class="quiz">',
  'lab':'<tr class="lab">',
  'holiday':'<tr class="holiday">',
  'td':'<td>',
  'tablestart':'<table border="1" cellpadding="4" cellspacing="3" width="90%" align="center">',
  'tableend':'</table>',
  'tablehead':'<tr bgcolor="#ffcc33"><th>Class#<th>Date<th>Topic<th>Handouts,<br>Assignments<th>Notes'
}

def printHeader(course_num='1234', course_name="DEFAULT", quarter="NONE"):
  print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
   "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
  <meta http-equiv=Content-Type content="text/html; charset=iso-8859-1">
  <meta http-equiv="cache-control" content="no-cache">
  <meta http-equiv="cache-control" content="no-store">
  <meta http-equiv="pragma" content="no-cache">
  <meta http-equiv="expires" content="-1">
  <link rel="stylesheet" href="main.css" type="text/css">
""")
  print("<title>",course_num,"Schedule</title></head>")
  print('<body bgcolor="white" link="blue" vlink="blue">')
  print("<h3 align=center>",course_num, course_name,"("+quarter+")</h3>")

def printNote(course_num="1234"):
  print("<p><u>",course_num,"students -- Please note:</u>")
  print("""
<ol start=1 type=1>
 <li>Lecture numbers (L1, L2, etc.) are linked to corresponding
     lecture notes.  Generally, these will appear on this page
     soon after the lecture.  Not all notes are in flowing text;
     usually they are in bullet form and highlight things we
     consider important about the area being discussed.</li>
 <li>For all lectures, you MUST try and read the assigned papers
     and/or textbook section
     BEFORE lecture.  You're likely to get the most out of each
     lecture if you read the material beforehand.</li>
 <li>Pay attention to the due dates for homeworks, labs, and
     other deadlines.  All deadlines are hard.</li>
</ol>
""")

def printFooter():
  print("""
<br>
<b>All notes are Copyright &copy;2011-2019 Robert Beverly</b>
<p>
<i>Permission to make digital or hard copies of part or all
of this work for personal use is granted without fee provided that copies are
not made or distributed for profit or commercial advantage and that the
copyright notice appears on the first page. Permission to make digital or hard
copies of part or all of this work for classroom use requires prior specific
permission and should include the copyright notice on the first page. To copy
otherwise, to republish, to post on servers, or to redistribute to lists,
requires prior specific permission and/or a fee.</i> 

</body>
<head>
  <META HTTP-EQUIV="PRAGMA" CONTENT="NO-CACHE">
</head>
</html>
""")

def printLecture(num, d, name, assign, note, head=None):
  if name.lower().find("quiz") != -1:
    print(flair['quiz'])
  elif name.lower().find("exam") != -1:
    print(flair['quiz'])
  elif head:
    print(head)
  else:
    print(flair['treven'])
  if num == 0:
     num = '-'
  print(flair['td'], num, flair['td'], end=' ') 
  print(d.strftime('%a %m/%d'))
  print(flair['td'], name)
  print(flair['td'])
  if assign: print(assign)
  print(flair['td'])
  if note: print(note)

def main():
  sys.path.insert(1,os.getcwd())
  import course
  printHeader(course.num, course.name, course.quarter)
  printNote(course.num)
  print("Last updated:", time.asctime(time.localtime()))
  print(flair['tablestart'])
  print(flair['tablehead'])
  lecture_date = course.first_lecture
  lecture = 0
  lab = 0
  while lecture_date <= course.last_lecture:
    if lecture_date in course.skip:
      lecture_date = lecture_date + timedelta(days=1)
      continue
    if lecture >= len(course.lectures): 
      course.lectures.append("N/A")
      print("Potential Problem: too few lectures!", len(course.lectures), lecture, file=sys.stderr)
    if lab >= len(course.labs):
      course.labs.append("N/A")
      print("Potential Problem: too few labs!", len(course.labs), lab, file=sys.stderr)
    assign = None
    if lecture_date in course.assignments:
      assign = course.assignments[lecture_date]
    note = None 
    if lecture_date in course.notes:
      note = course.notes[lecture_date]
    if lecture_date in course.holidays:
      printLecture(0, lecture_date, course.holidays[lecture_date], assign, note, flair['holiday'])
    elif lecture_date in course.final:
      printLecture(lecture+1, lecture_date, course.final[lecture_date], assign, note, flair['odd'])
      lecture+=1
#    elif lecture_date in course.extralab:
#      assign = course.assignments_labs[lecture_date]
#      printLecture("L" + str(lab+1), lecture_date, course.labs[lab], assign, note, flair['lab'])
#      lab+=1
    elif course.lecture_days[lecture_date.weekday()]:
      if course.lectures[lecture].lower().find("quiz") != -1:
        printLecture(lecture+1, lecture_date, course.lectures[lecture], assign, note, flair['quiz'])
      elif (lecture+1) % 2 == 0:
        printLecture(lecture+1, lecture_date, course.lectures[lecture], assign, note, flair['even'])
      else:
        printLecture(lecture+1, lecture_date, course.lectures[lecture], assign, note, flair['odd'])
      lecture+=1
    if course.lab_days[lecture_date.weekday()] and lecture_date not in course.holidays:
      if lecture_date in course.assignments_labs:
        assign = course.assignments_labs[lecture_date]
        note = None
      else:
        assign = None
      printLecture("L" + str(lab+1), lecture_date, course.labs[lab], assign, note, flair['lab'])
      lab+=1
    lecture_date = lecture_date + timedelta(days=1)
  print(flair['tableend'])
  printFooter()

if __name__=="__main__":
  main()
