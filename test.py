def findEncodings (images):
    encodelist = []
    for img in images:
        img =cv2.cvtColor(imgcv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open(Attendance.csv) as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.spilt(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime,now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'/n')
            cv2.imshow('test',imgTest)
            results = face_recognition.compare_faces([encodeElon],encodeTest)
            faceDis = face_recognition.face_distance([encodeElon],encodeTest)
        return results
def captureScreen:
    