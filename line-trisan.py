# -*- coding: utf-8 -*-
import LINETCR
from LINETCR.lib.curve.ttypes import *
from io import StringIO
from datetime import datetime
import time,requests,urllib,random,sys,json,codecs,threading,glob,sys
import re,ast,string,os
import os.path,sys,urllib,urllib2,shutil,subprocess

cl = LINETCR.LINE()
cl.login(token="EmJUlnlkjvXJq4lMDK5.5Cu7yw/ipCUcuMRsS8zVfq.W2yazplz78zkTk/bqcuO8MTx13hr3mwaToo8Gx44nDI=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="En6luANG5t5PwnLG081.82YW3sF0Bn7sgQxY5sxbCq.nxCWsVYHRAfux21cQIvPNdiWvsKbEEG0kgAhM8268uw=")
ki.loginResult()

kk = LINETCR.LINE()
kk.login(token="EmwBCxE06SJvxgx1oVi6.iPBRR1RMNZ6JK83Lr8Y1G.vjv3plNJlURcg064ojglt80/V1hrnKodi9gg8E04wAk=")
kk.loginResult()

kc = LINETCR.LINE()
kc.login(token="EmAc5fKepHjFNBfMHdz8.JML4H1XdaTwzSRX/sR/ka.nvLTzV7C0yCX4kDF/u/Ps/d+A6R+YzpRveAjnKUQbcU=")
kc.loginResult()

ke = LINETCR.LINE()
ke.login(token="EnfxhZKwcZSx68OMTa61.HmbgfWQSObUqoejBqKjuyq.oaefT6yehtzr9Z3kvQBh1TNyVdir1kbSH+SV0J/uMM=")
ke.loginResult()

ko = LINETCR.LINE()
ko.login(token="EnwCdpmDPFkEBdqhJ4e6.8TpVl4F/azavSAKKbg6bG.l4nkxI3D9+dYw76b/AhFmNc78hrgPoElfQ6/Od0gZb0=")
ko.loginResult()

ks = LINETCR.LINE()
ks.login(token="Em9gHjjS6WemwzWn4bK5.C14lfzxM4FuxU2yIWHg5q.99pN2k7l0wMD/4JWgdAtU5ced1JBXLq5ZpZg7vTiACo=")
ks.loginResult()

ku = LINETCR.LINE()
ku.login(token="EmWzT6bEM08wY3sczrp4.FFsjh5E9IQTr87JOu0g1a.Wpxakc1ZnYcX/TQIKdZE3erYiDQx+dBRjOVOIikbmcs=")
ku.loginResult()

ka = LINETCR.LINE()
ka.login(token="EnE2ydI48WHdR9457tOe.rHrHCJlFm9PiD3fCm6pNG.NC+2FOuDOgSJmyfLbAq4k+G1bkL7bxVvJFnOBlhXcd0=")
ka.loginResult()

kb = LINETCR.LINE()
kb.login(token="EmVRXTqo1mlqtcaAByQ8.D6VIpSM2otkTCurxH4q/a./EInNotVyh9oxTpZbXTHTl3bnbCdShvpwLbvl9fduE0")
kb.loginResult()

b1 = LINETCR.LINE()
b1.login(token="EndFmJBugo12IdPFKOQ4.xWk4769z47gTIM2HcShHa.VcQyp9Y4r7EVeQsmnoFwrmhFVWbTL8zuqsZoNCXzD5g=")
b1.loginResult()

k1 = LINETCR.LINE()
k1.login(token="EnY2jsutPUUM1aSvg7Pf.LrkxplhqaEVpA3t5C4bSJW.j7IpWX7amUgMGGETmZ4r2j+CwwfV4MZGQdqv0zt+nhY=")
k1.loginResult()

mj = LINETCR.LINE()
mj.login(token="En7KnCQk1lx91KnGvZT1.kF2FXVi4PyP6crs9fN00q.kLN+fmfFOQDihYEhDdpx4Sk4/mYsbeqVJaGtShX8nUU=")
mj.loginResult()

k2 = LINETCR.LINE()
k2.login(token="EnSrcUrGy1UlRHYdHuj9.VWtBSximFtqX1daFa0VL6.njvNRNcuNzgEbj/PmSxHm2JVc/VBY5qrIzuCYfrmZ2o=")
k2.loginResult()

k3 = LINETCR.LINE()
k3.login(token="EnZvoE9qEzOin790lPf1.ZySAgXWuzXIRX2B8heRO4q.m7QZSKUHSCM6ghAjgdDsJXEAXKZcV2D5EYC0xW5c5/8=")
k3.loginResult()

k4 = LINETCR.LINE()
k4.login(token="EnqkO8AUmf7GG39GT5F1.QJXDeKNiHqdstWvfOepOq.L4TfYYOSiaWmPnCP4f58BFsLOkjwPJoZvOS1ZkN0lTY=")
k4.loginResult()
# client_id = ''
# client_secret = ''
# access_token = ''
# client = ImgurClient(client_id, client_secret, access_token)
print "BOT TRISAN SUKSES LOGIN"
reload(sys)
sys.setdefaultencoding('utf-8')
album = None
image_path = 'tmp/tmp.jpg'
helpMessage ="""❂͜͡☆❂͜͡☆❂͜͡☆ɞȏṭ קяȏṭєċṭ❂͜͡☆❂͜͡☆❂͜͡☆
-===================-
◄]·♦·»Menu For Public«·♦·[►
[•]Gcreator ► Pembuat Grup
[•]Respon ► Bot
[•]Ginfo ►info Grup
[•]K on ► Contact On
[•]K off ►Contact off
[•]Sp / Speed ► Kecepatan Respon
[•]Ourl ► open QR (New Protect QR)
[•]Gift ► Mengirim Hadiah
[•]Ban @ ► blokir
[•]Unban @ ► Membuka Ban/Blacklist
[•]Apakah ► Kerang Ajaib
[•]Rate ►  % 
[•]Mugiwara bye ►
[•]Creator1►
[•]Cctv » ReadRom
[•]Ciduk = Cek Sider
-===================-
◄]·♦·»BOT Public«·♦·[►     
-===================-
-===================-
"""
KAC=[cl,ki,kk,kc,ko,ks,ka,kb,ke,ku,k1,mj,k2,k3,k4,b1]
Bots=[cl,ki,kk,kc,ko,ks,ka,kb,ke,ku,k1,mj,k2,k3,k4,b1]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Gmid = ko.getProfile().mid
Dmid = ks.getProfile().mid
Emid = ka.getProfile().mid
Fmid = kb.getProfile().mid
Hmid = ke.getProfile().mid
Imid = ku.getProfile().mid
Kmid = k1.getProfile().mid
Mmid = mj.getProfile().mid
Kmid = k3.getProfile().mid
K2mid = k2.getProfile().mid
K4mid = k4.getProfile().mid
B1mid = b1.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid,Gmid,Dmid,Emid,Fmid,Hmid,Kmid,Mmid,Kmid,K2mid,B1mid,K4mid,"ue5c53b616f883dcb82526ad2b3c66f15"]
admin=["uba553877e995e2bd476d1d78469dc8d2","ue5c53b616f883dcb82526ad2b3c66f15","u9512973cb1d001ebcf6b74f973806c8f","ubf04dbb1720c7d3431d4301f034be5e9","u5f02b8efaf59e3b1ad8a6da10ac1da84","ucd8b1a1b1c146718abc766fc1c4ae8e1","u7df4891f97bd8aab51f3b8e8534106d4","u84c046170aaca01b9038425b42425461","u77abe23ec9b63932ad714457878bd0f8","u4614617232df33da4877715c33ae4f9e","u735e0b1595e6e1f517bb6622830846e5","u8e6978875c4302d599b3daf1f92afe28","uf2d3ef2f87fe019015b1a9240011ba06","u2296eb02bd6b9a7cfa8e4f37951f32d6","uf36cb0dd27f46cded21aa5f2e525c171","u1b9ab645520fa5ae9d734f6e6b9b56ba","ufa6afcbcac1bbfbc80008a6aebad5b27","u0489c1e5714d680431783066fbfdad8a"]
creator=["uba553877e995e2bd476d1d78469dc8d2","u1b9ab645520fa5ae9d734f6e6b9b56ba"]
owner=["uba553877e995e2bd476d1d78469dc8d2"]
me = cl.getProfile().mid
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':"Creator add : line://ti/p/~mtrisan",
    "lang":"JP",
    "comment":"Creator : line://ti/p/~mtrisan",
    "commentOn":True,
    "likeon":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"¹Xplyer ا ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "ProtectQR":False,
    "Protectjoin":True,
    "Protectguest":False,
    "Protectcancel":True,
    "atjointicket":True,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ProtectQR':{},
    'ROM':{}
    }

mimic = {
    "copy":True,
    "copy2":True,
    "status":True,
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']

res = {
    'num':{},
    'us':{},
    'au':{},
}
fastbinary = None
mulai = time.time()
contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def Cmd(string, commands):
    tex = [""]
    for texX in tex:
        for command in command:
            if string ==texX + command:
                return True
    return False
def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '||(%02d Jam)•(%02d Menit)•(%02d Detik)||' % (hours, mins, secs)

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    print nm
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "◈ @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention」\n"+bb
    msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
         cl.sendMessage(msg)
    except Exception as error:
        print error 

def NOTIFIED_READ_MESSAGE(op):
    #print op
    try:
        if op.param1 in readPoint['readPoint']:
            Name = client.getContact(op.param2).displayName
            if Name in wait['readMember'][op.param1]:
                pass
            else:
                wait['readMember'][op.param1] += "\n・" + Name
                wait['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait['readPoint']:
                    if msg.from_ in wait["ROM"][msg.to]:
                        del wait["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
    except KeyboardInterrupt:
           sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
         #------Open QR Kick start------#
        if op.type == 10:
           if wait["ProtectQR"] == True:
               if op.param2 not in Bots:
                   G = cl.getGroup(op.param1)
                   G = ki.getGroup(op.param1)
                   G.preventJoinByTicket = True
                   ka.kickoutFromGroup(op.param1,[op.param2])
                   cl.updateGroup(G)
        #------Open QR Kick finish-----#

        #------Invite User Kick start------#
        if op.type == 13:
           if wait["Protectguest"] == True:
            if op.param2 not in Bots:
              group = cl.getGroup(op.param1)
              gMembMids = [contact.mid for contact in group.invitee]
              random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Invite User Kick Finish------#

        #------Joined User Kick start------#
        if op.type == 13: #awal 17 ubah 13
           if wait["Protectjoin"] == True:
               if op.param2 not in admin and Bots : # Awalnya admin doang
                   random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Joined User Kick start------#


        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = cl.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n[•]" + Name
                wait2['ROM'][op.param1][op.param2] = "[•]" + Name
            else:
              cl.sendText
          except:
             pass

        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                if op.param3 in Dmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        ks.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ks.updateGroup(X)
                        Ti = ks.reissueGroupTicket(op.param1)
                if op.param3 in Gmid:
                    if op.param2 in Fmid:
                        X = kb.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kb.updateGroup(X)
                        Ti = kb.reissueGroupTicket(op.param1)
                        ko.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ko.updateGroup(X)
                        Ti = ko.reissueGroupTicket(op.param1)
                if op.param3 in Emid:
                    if op.param2 in Dmid:
                        X = ks.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ks.updateGroup(X)
                        Ti = ks.reissueGroupTicket(op.param1)
                        ka.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ka.updateGroup(X)
                        Ti = ka.reissueGroupTicket(op.param1)
                if op.param3 in Cmid:
                    if op.param2 in Fmid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                if op.param3 in Fmid:
                    if op.param2 in Emid:
                        X = ka.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ka.updateGroup(X)
                        Ti = ka.reissueGroupTicket(op.param1)
                        kb.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kb.updateGroup(X)
                        Ti = kb.reissueGroupTicket(op.param1)
                if op.param3 in Hmid:
                    if op.param2 in Imid:
                        X = ko.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ko.updateGroup(X)
                        Ti = ko.reissueGroupTicket(op.param1)
                        ke.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ke.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)
                if op.param3 in Imid:
                    if op.param2 in Kmid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        ku.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                if op.param3 in Kmid:
                    if op.param2 in Kmid:
                        X = k1.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        k1.updateGroup(X)
                        Ti = k1.reissueGroupTicket(op.param1)
                        kj.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = k1.reissueGroupTicket(op.param1)
                if op.param3 in Kmid:
                    if op.param2 in Mmiid:
                        X = k3.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        k3.updateGroup(X)
                        Ti = k3.reissueGroupTicket(op.param1)
                        k3.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = k3.reissueGroupTicket(op.param1)
                if op.param3 in Mmid:
                    if op.param2 in K2mid:
                        X = mj.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        mj.updateGroup(X)
                        Ti = mj.reissueGroupTicket(op.param1)
                        mj.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = mj.reissueGroupTicket(op.param1)
                if op.param3 in K2mid:
                    if op.param2 in K4mid:
                        X = k2.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        k2.updateGroup(X)
                        Ti = k2.reissueGroupTicket(op.param1)
                        k2.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = k2.reissueGroupTicket(op.param1)
                if op.param3 in K4mid:
                    if op.param2 in mid:
                        X = k4.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        k4.updateGroup(X)
                        Ti = k4.reissueGroupTicket(op.param1)
                        k4.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = k4.reissueGroupTicket(op.param1)
                if op.param3 in B1mid:
                    if op.param2 in mid:
                        X = b1.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        b1.updateGroup(X)
                        Ti = b1.reissueGroupTicket(op.param1)
                        b1.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = c1.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    ki.cancelGroupInvitation(op.param1, matched_list)
                    kk.cancelGroupInvitation(op.param1, matched_list)
                    ks.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 11:
                if op.param2 not in Bots:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = True
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        k1.acceptGroupInvitationByTicket(op.param1, Ticket)
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.leaveGroup(op.param1)
                        cl.updateGroup(G)
                        x = Message(to=op.param1, from_=None, text=None, contentType=13)
                        x.contentMetadata={'mid':op.param2}
                        cl.sendMessage(x)
                        wait["blacklist"][op.param2] = True
                        print "kicker"

        if op.type == 32:
                if not op.param2 in Bots and admin:
                    if wait["protectionOn"] == True: 
                        try:
                            klist=[ki,kk,kc,ke,ko,ks,ku,ka,kb,b1,k1,mj,k2,k3,k4]
                            kicker = random.choice(klist) 
                            G = cl.getGroup(op.param1)
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                            wait["blacklist"][op.param2] = True
                            print "kicker"
                        except Exception, e:
                            print e

        if op.type == 19:
          if op.param3 in admin: #Kalo Admin ke Kick
            if op.param2 in Bots:
              pass
            if op.param2 in owner:
              pass
            else:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                cl.inviteIntoGroup(op.param1,[op.param3])

        if op.type == 19:
                if op.param2 not in admin:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    print "kicker"
                else:
                    pass

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    mj.acceptGroupInvitationByTicket(op.param1,Ti)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    k4.acceptGroupInvitationByTicket(op.param1,Ti)
                    b1.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    mj.acceptGroupInvitationByTicket(op.param1,Ti)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    k4.acceptGroupInvitationByTicket(op.param1,Ti)
                    b1.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        ks.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    mj.acceptGroupInvitationByTicket(op.param1,Ti)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    k4.acceptGroupInvitationByTicket(op.param1,Ti)
                    b1.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        ka.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    mj.acceptGroupInvitationByTicket(op.param1,Ti)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    k4.acceptGroupInvitationByTicket(op.param1,Ti)
                    b1.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ks.kickoutFromGroup(op.param1,[op.param2])
                        ka.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    mj.acceptGroupInvitationByTicket(op.param1,Ti)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    k4.acceptGroupInvitationByTicket(op.param1,Ti)
                    b1.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ks.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ks.updateGroup(G)
                    Ticket = ks.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        kb.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    X = ka.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    mj.acceptGroupInvitationByTicket(op.param1,Ti)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    k4.acceptGroupInvitationByTicket(op.param1,Ti)
                    b1.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ka.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ka.updateGroup(G)
                    Ticket = ka.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        ko.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    X = kb.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    mj.acceptGroupInvitationByTicket(op.param1,Ti)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    k4.acceptGroupInvitationByTicket(op.param1,Ti)
                    b1.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kb.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kb.updateGroup(G)
                    Ticket = kb.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ko.kickoutFromGroup(op.param1,[op.param2])
                        ke.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    X = ko.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = ko.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    mj.acceptGroupInvitationByTicket(op.param1,Ti)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    k4.acceptGroupInvitationByTicket(op.param1,Ti)
                    b1.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ko.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ko.updateGroup(G)
                    Ticket = ko.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Hmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        k1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    X = ke.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    mj.acceptGroupInvitationByTicket(op.param1,Ti)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    k4.acceptGroupInvitationByTicket(op.param1,Ti)
                    b1.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ke.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ke.updateGroup(G)
                    Ticket = ke.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Mmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        mj.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    mj.acceptGroupInvitationByTicket(op.param1,Ti)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    k4.acceptGroupInvitationByTicket(op.param1,Ti)
                    b1.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ke.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ke.updateGroup(G)
                    Ticket = ke.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Mmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k3.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    mj.acceptGroupInvitationByTicket(op.param1,Ti)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    k4.acceptGroupInvitationByTicket(op.param1,Ti)
                    b1.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = mj.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    mj.updateGroup(G)
                    Ticket = mj.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Kmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k2.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    mj.acceptGroupInvitationByTicket(op.param1,Ti)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    k4.acceptGroupInvitationByTicket(op.param1,Ti)
                    b1.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = k3.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    k3.updateGroup(G)
                    Ticket = k3.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if K2mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k4.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    mj.acceptGroupInvitationByTicket(op.param1,Ti)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    k4.acceptGroupInvitationByTicket(op.param1,Ti)
                    b1.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = k2.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    Ticket = k2.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if K4mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        b1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    mj.acceptGroupInvitationByTicket(op.param1,Ti)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    k4.acceptGroupInvitationByTicket(op.param1,Ti)
                    b1.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = k4.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    k4.updateGroup(G)
                    Ticket = k4.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
                midd = msg.text.replace("Kick ","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Nami invite " in msg.text:
                midd = msg.text.replace("Nami invite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "Zoro invite " in msg.text:
                midd = msg.text.replace("Zoro invite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "Trisan invite " in msg.text:
                midd = msg.text.replace("Trisan invite ","")
                k1.findAndAddContactsByMid(midd)
                k1.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '2580c0e3-0c4e-48df-903f-2e7dc7d5595f',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["cancel","Cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cancel2","cancel2"]:
                if msg.toType == 2:
                    G = k3.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        k3.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            k3.sendText(msg.to,"No one is inviting")
                        else:
                            k3.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        k3.sendText(msg.to,"Can not be used outside the group")
                    else:
                        k3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Ourl","Link on"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Curl","Link off"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.id,ticket_id)
				cl.sendText(msg.to,"Sukses join %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "925",
                                     "STKPKGID": "14319",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cnder "]:
                string = msg.text.replace("Cnder ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Menju"]:
              if msg.from_ in admin:
                string = msg.text.replace("哦上的 ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = k4.getProfile()
                    profile_B.displayName = string
                    k4.updateProfile(profile_B)
                    k4.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["AuThenTic"]:
              if msg.from_ in admin:
                string = msg.text.replace("哦上的 ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = k1.getProfile()
                    profile_B.displayName = string
                    k1.updateProfile(profile_B)
                    k1.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)

            elif msg.text in ["Guest On","guest on"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Guest Off","guest off"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr on","qr on"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr off","qr off"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")

            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ³","K on","Contact on","é¡¯ç¤ºï¼šé–‹"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ•","K off","Contact off","é¡¯ç¤ºï¼šé—œ"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•åƒåŠ ï¼šé–‹"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•åƒåŠ ï¼šé—œ"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["Lroom off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["/set"]:
                if msg.from_ in admin:
		    md = ""
		    if wait["contact"] == True: md+=" [•]Contact ➣ on\n"
		    else: md+=" [•]Contact ➣ off\n"
		    if wait["autoJoin"] == True: md+=" [•]Auto join ➣ on\n"
		    else: md +=" [•]Auto join ➣ off\n"
		    if wait["autoCancel"]["on"] == True:md+=" [•]Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
		    else: md+= " [•]Group cancel ➣ off\n"
		    if wait["leaveRoom"] == True: md+=" [•]Auto leave ➣ on\n"
		    else: md+=" [•]Auto leave ➣ off\n"
		    if wait["timeline"] == True: md+=" [•]Share ➣ on\n"
		    else:md+=" [•]Share ➣ off\n"
		    if wait["autoAdd"] == True: md+=" [•]Auto add ➣ on\n"
		    else:md+=" [•]Auto add ➣ off\n"
		    if wait["commentOn"] == True: md+=" [•]Comment ➣ on\n"
		    else:md+=" [•]Comment ➣ off\n"
		    if wait["Protectcancel"] == True: md+=" [•]Mad ➣ on\n"
		    else:md+=" [•]Mad ➣ off\n"
		    if wait["Protectguest"] == True: md+=" [•]Guest ➣ on\n"
		    else:md+=" [•]Guest ➣ off\n"
		    if wait["atjointicket"] == True: md+=" [•]Auto Join Group by Ticket ➣ on\n"
		    else:md+=" [•]Auto Join Group by Ticket ➣ off\n"
		    cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id","ç¾¤çµ„å…¨id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeâ†’" in msg.text:
                gid = msg.text.replace("album removeâ†’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é ç•™è¨€ï¼šé–‹"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment on","Comment off","è‡ªå‹•é¦–é ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot1 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot2 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot3 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kc.updateGroup(x)
                    gurl = kc.reissueGroupTicket(msg.to)
                    kc.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Change clock "]:
                n = msg.text.replace("Change clock ","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
#-----------------------------------------------

            elif msg.text.lower() == 'runtime':
                    eltime = time.time() - mulai
                    van = "Mugiwara Bertempur Selama "+waktu(eltime)
                    cl.sendText(msg.to,van)
#-----------------------------------------------

            elif "/joingc: " in msg.text:
              if msg.from_ in admin:
                gid = msg.text.replace("/joingc: ","")
                if gid == "":
                  cl.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    cl.findAndAddContactsByMid(msg.from_)
                    cl.inviteIntoGroup(gid,[msg.from_])
                  except:
                    cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#-----------------------------------------------

            elif msg.text == "Cctv":
                cl.sendText(msg.to, "Cek CCTV ketik *Ciduk* Untuk melihat Sider")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
                  pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                wait2['ROM'][msg.to] = {}
                #print wait2
              
            elif msg.text == "Ciduk":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                #print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "╔═══════════════%s\n╠════════════════\n%s╠═══════════════\n║Reading point creation:\n║ [%s]\n╚════════════════\n||BOT Public||" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik Cctv dulu Koplak\nBaru Ketil Ciduk\nDASAR PIKUN ♪")
#-----------------------------------------------

            elif msg.text in ["Bot out","Op bye"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = kk.getGroupIdsJoined()
                gid = kc.getGroupIdsJoined()
                gid = ks.getGroupIdsJoined()
                gid = ko.getGroupIdsjoined()
                gid = ka.getGroupIdsjoined()
                git = kb.getGroupIdsjoined()
                git = ke.getGroupIdsjoined()
                git = ku.getGroupIdsjoined()
                git = k1.getGroupIdsjoined()
                git = k3.getGroupIdsjoined()
                git = k2.getGroupIdsjoined()
                git = b1.getGroupIdsjoined()
                for i in gid:
                  ks.leaveGroup(i)
                  kc.leaveGroup(i)
                  ki.leaveGroup(i)
                  kk.leaveGroup(i)
                  ko.leaveGroup(i)
                  ka.leaveGroup(i)
                  kb.leaveGroup(i)
                  ke.leaveGroup(i)
                  ku.leaveGroup(i)
                  k1.leaveGroup(i)
                  k3.leaveGroup(i)
                  k2.leaveGroup(i)
                  b1.leaveGroup(i)
                  cl.leaveGroup(i)
                if wait["lang"] == "JP":
                  cl.sendText(msg.to,"Sedang Ada Perbaikan R lagi iya Nanti")
                else:
                  cl.sendText(msg.to,"He declined all invitations")
#-----------------------------------------------

            elif msg.text in ["@bot out"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                gid = cl.sendText(msg.to,"Sistem Error silahkan Reinvit Beberapa menit lagi.")
                for i in gid:
                  cl.leaveGroup(i)
                if wait["lang"] == "JP":
                  cl.sendText(msg.to,"Tidak ada Bos!!")
                else:
                  cl.sendText(msg.to,"He declined all invitations")
#-----------------------------------------------

            elif "/movechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        cl.removeAllMessages(op.param2)
                        ki.removeAllMessages(op.param2)
                        kk.removeAllMessages(op.param2)
                        k2.removeAllMessages(op.param2)
                        k3.removeAllMessages(op.param2)
                        k4.removeAllMessages(op.param2)
                        kc.removeAllMessages(op.param2)
                        ko.removeAllMessages(op.param2)
                        ks.removeAllMessages(op.param2)
                        ka.removeAllMessages(op.param2)
                        kb.removeAllMessages(op.param2)
                        ke.removeAllMessages(op.param2)
                        ku.removeAllMessages(op.param2)
                        k1.removeAllMessages(op.param2)
                        mj.removeAllMessages(op.param2)
                        b1.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        cl.sendText(msg.to,"RemoveChat Done Bos!!")
                    except Exception as error:
                        print error
                        cl.sendText(msg.to,"LineError")
#-----------------------------------------+++---

            elif msg.text in ["Tagall"]:
              if msg.from_ in admin:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(5)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(6)
                    akh = akh + 1
                    cb2 += "@nrik\n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    ki.sendMessage(msg)
                except Exception as error:
                    print error
#-----------------------------------------------
            elif msg.text in ["Mugiwara join"]:
              if msg.from_ in admin:
                G = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                G.preventJoinByTicket = False
                cl.updateGroup(G)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                ku.acceptGroupInvitationByTicket(msg.to,Ticket)
                b1.acceptGroupInvitationByTicket(msg.to,Ticket)
                k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                mj.acceptGroupInvitationByTicket(msg.to,Ticket)
                k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                G = cl.getGroup(msg.to)
                G.preventJoinByTicket = True
                ki.updateGroup(G)
                G.preventJoinByTicket(G)
                kk.updateGroup(G)
                print "Mugiwara join"

            elif msg.text in ["Der1"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)

            elif msg.text in ["Der2"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)

#-----------------------------------------------
#.acceptGroupInvitationByTicket(msg.to,Ticket)
            elif msg.text in ["Der3 join"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "Mugiwara join"
                        G.preventJoinByTicket = True
                        kc.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["Mugiwara bye"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                        kb.leaveGroup(msg.to)
                        ko.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        ku.leaveGroup(msg.to)
                        b1.leaveGroup(msg.to)
                        k4.leaveGroup(msg.to)
                        k2.leaveGroup(msg.to)
                        mj.leaveGroup(msg.to)
                        k1.leaveGroup(msg.to)
                        k3.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["//Bye"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to,)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["Kill"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kk.sendText(msg.to,"Fuck You")
                        kc.sendText(msg.to,"Fuck You")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,kk,kc]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "Room." in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Room.","")
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    ki.sendText(msg.to,"Ini Room apa? ? Mugiwara Sita!!")
                    cl.sendText(msg.to,"Group Di Sita.")
                    k4.sendText(msg.to,"Rata Gak Rata")
                    kc.sendText(msg.to,"Kita Mampir Menghibur Kalian")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                klist=[ki,kk,kc,k1,k4,cl]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg.to,"Group Disita")

            elif "Nk " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl,ki,kk,kc]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    kk.sendText(msg.to,"Fuck You")
            elif "Blacklist @ " in msg.text:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = ki2.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    k3.sendText(msg.to,"Succes ")
                                except:
                                    ki.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        print "[Ban]ok"
                        _name = msg.text.replace("Ban @","")
                        _nametarget = _name.rstrip('  ')
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Not found ")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Succes ")
                                except:
                                    ki.sendText(msg.to,"Error")
#-----------------------------------------------
            elif "Ban all" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        print "[Ban]ok"
                        _name = msg.text.replace("Ban all","")
                        gs = cl.getGroup(msg.to)
                        cl.sendText(msg.to,"BL Succes💀")
                        targets = []
                        for g in gs.members:
                                if _name in g.displayName:
                                        targets.append(g.mid)
                        if targets == []:
                                cl.sendText(msg.to,"Tidak Ada Boss")
                        else:
                                for target in targets:
                                        try:
                                            wait["blacklist"][target] = True
                                            f=codecs.open('st2__b.json','w','utf-8')
                                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                        except:
                                            cl.sendText(msg.to,"Succes")
#-----------------------------------------------
            elif "Unban all" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        print "[Unban]ok"
                        _name = msg.text.replace("Unban all","")
                        gs = cl.getGroup(msg.to)
                        cl.sendText(msg.to,"BL Delete")
                        targets = []
                        for g in gs.members:
                                if _name in g.displayName:
                                        targets.append(g.mid)
                        if targets == []:
                                cl.sendText(msg.to,"Tidak Ada Boss Owner")
                        else:
                                for target in targets:
                                        try:
                                            del wait["blacklist"][target]
                                            f=codecs.open('st2__b.json','w','utf-8')
                                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                        except:
                                            cl.sendText(msg.to)
#-----------------------------------------------

            elif "Mid @" in msg.text:
        	if msg.from_ in admin:
                  _name = msg.text.replace("Mid @","")
                  _nametarget = _name.rstrip(' ')
                  gs = cl.getGroup(msg.to)
                  for g in gs.members:
                      if _nametarget == g.displayName:
                          cl.sendText(msg.to, g.mid)
                      else:
                          pass
#-----------------------------------------------
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found ")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Succes ")
                            except:
                                ki.sendText(msg.to,"Succes ")
#-----------------------------------------------
            elif "Glist" in msg.text:
                if msg.from_ in admin:
                        gid = cl.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            h += "=> %s  \n" % (cl.getGroup(i).name + " | Members : [ " + str(len (cl.getGroup(i).members))+" ]")
                        cl.sendText(msg.to, "#[List Grup]# \n"+ h +"Total Group : " +"[ "+str(len(gid))+" ]")
                        print "Glist"
#-----------------------------------------------
            elif msg.text in ["Gcreator:inv"]:
               if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
                       
            elif msg.text in ["Gcreator"]:
              if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName
                        
                    except:
                        gCreator = "Error"
                    cl.sendText(msg.to, "Group Creator : " + gCreator1)
                    cl.sendMessage(msg)
#-----------------------------------------------

            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
        	text = msg.text
        	if text is not None:
        	    cl.sendText(msg.to,text)
        	else:
        	    if msg.contentType == 7:
        		msg.contentType = 7
        		msg.text = None
        		msg.contentMetadata = {
        				     "STKID": "6",
        				     "STKPKGID": "1",
        				     "STKVER": "100" }
        		cl.sendMessage(msg)
        	    elif msg.contentType == 13:
        		msg.contentType = 13
        		msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
        		cl.sendMessage(msg)
            elif "Mimic:" in msg.text:
        	if msg.from_ in admin:
        	    cmd = msg.text.replace("Mimic:","")
        	    if cmd == "on":
        		if mimic["status"] == False:
        		    mimic["status"] = True
        		    cl.sendText(msg.to,"Mimic on")
        		else:
        		    cl.sendText(msg.to,"Mimic already on")
        	    elif cmd == "off":
        		if mimic["status"] == True:
        		    mimic["status"] = False
        		    cl.sendText(msg.to,"Mimic off")
        		else:
        		    cl.sendText(msg.to,"Mimic already off")
        	    elif "add:" in cmd:
        		target0 = msg.text.replace("Mimic:add:","")
        		target1 = target0.lstrip()
        		target2 = target1.replace("@","")
        		target3 = target2.rstrip()
        		_name = target3
        		gInfo = cl.getGroup(msg.to)
        		targets = []
        		for a in gInfo.members:
        		    if _name == a.displayName:
        			targets.append(a.mid)
        		if targets == []:
        		    cl.sendText(msg.to,"No targets")
        		else:
        		    for target in targets:
        			try:
        			    mimic["target"][target] = True
        			    cl.sendText(msg.to,"Success added target")
        			    #cl.sendMessageWithMention(msg.to,target)
        			    break
        			except:
        			    cl.sendText(msg.to,"Failed")
        			    break
        	    elif "del:" in cmd:
        		target0 = msg.text.replace("Mimic:del:","")
        		target1 = target0.lstrip()
        		target2 = target1.replace("@","")
        		target3 = target2.rstrip()
        		_name = target3
        		gInfo = cl.getGroup(msg.to)
        		targets = []
        		for a in gInfo.members:
        		    if _name == a.displayName:
        			targets.append(a.mid)
        		if targets == []:
        		    cl.sendText(msg.to,"No targets")
        		else:
        		    for target in targets:
        			try:
        			    del mimic["target"][target]
        			    cl.sendText(msg.to,"Success deleted target")
        			    #cl.sendMessageWithMention(msg.to,target)
        			    break
        			except:
        			    cl.sendText(msg.to,"Failed!")
        			    break
        	    elif cmd == "ListTarget":
        		if mimic["target"] == {}:
        		    cl.sendText(msg.to,"No target")
                        else:
                	    lst = "<<Lit Target>>"
                	    total = len(mimic["target"])
                	    for a in mimic["target"]:
            		        if mimic["target"][a] == True:
            			    stat = "On"
            		        else:
            			    stat = "Off"
            		        lst += "\n->" + cl.getContact(mi_d).displayName + " | " + stat
                                cl.sendText(msg.to,lst + "\nTotal:" + total)
#-----------------------------------------------
            elif msg.text in ["Mad On","mad on"]:
              if msg.from_ in admin:
                 if wait["Protectcancel"] == True:
                     if wait["lang"] == "JP":
                         cl.sendText(msg.to,"Dont cancel anyone ! cause me angry!")
                     else:
                         cl.sendText(msg.to,"done")
                 else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Mad Off","mad off"]:
              if msg.from_ in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"done")

            elif msg.text in ["Joinn on","joinn on"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Joinn off","joinn off"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
#-----------------------------------------------

            elif "Fuck " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif "Nami kick " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      ki.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif "Ussop kick " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      kk.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif "Robin kick " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      kc.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif "Luffy kick " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      ks.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif "Zoro kick " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      ka.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif "Sanji kick " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      kb.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
#-----------------------------------------------
            elif msg.text in ["/Respon","/pesan"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"Mugiwara pirates respon all" )
                ki.sendText(msg.to,"Thunderbolt Tempo Hadir")
                kk.sendText(msg.to,"Hisatsu Hadir")
                ko.sendText(msg.to,"Yahazu Giri Hadir")
                kc.sendText(msg.to,"Fleur Hadir")
                ks.sendText(msg.to,"Gomu Gomu No Hadir")
                ka.sendText(msg.to,"Santoryu Hadir")
                kb.sendText(msg.to,"Diable Jambe Hadir")
                ke.sendText(msg.to,"Rumble Ball Hadir")
                ku.sendText(msg.to,"Franky Super Hadir")
                k3.sendText(msg.to,"ASL Hadir")
                b1.sendText(msg.to,"Hiken Hadir")
                k2.sendText(msg.to,"Bokapnya Luffy Hadir")
                k1.sendText(msg.to,"哦上的")
                k4.sendText(msg.to,"哦上的")
                mj.sendText(msg.to,"哦上的")
                print "/Respon"
#-----------------------------------------------
            elif msg.text in ["Creator"]:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "uba553877e995e2bd476d1d78469dc8d2"}
		    cl.sendMessage(msg)
            elif msg.text in ["Creator1"]:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "u1b9ab645520fa5ae9d734f6e6b9b56ba"}
		    cl.sendMessage(msg)
#-----------------------------------------------

            elif "Admin add @" in msg.text:
                if msg.from_ in creator:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admin add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Admin Ditambahkan")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command DiTolak")

            elif "Admin remove @" in msg.text:
                if msg.from_ in creator:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Admin remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Admin Dihapus")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command DiTolak")

            elif msg.text in ["Adminlist"]:
              if msg.from_ in creator:
                if admin == []:
                    cl.sendText(msg.to,"The adminlist is empty")
                else:
                    cl.sendText(msg.to,"Tunggu...")
                    mc = ""
                    for mi_d in admin:
                        mc += "➣"+cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
#-----------------------------------------------
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
#-----------------------------------------------

            elif "@Trisan " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("apa","pc aja")
                jawaban = random.choice(jawab)
                tts = gTTS(text=jawaban, lang='id')
                tts.save('tts.mp3')
                cl.sendAudio(msg.to,'tts.mp3')
#-----------------------------------------------

            elif "Mbc " in msg.text: #NgeBC Ke semua Group yang di Join :D
              if msg.from_ in admin:
                bctxt = msg.text.replace("Mbc ","")
                a = cl.getGroupIdsJoined()
                for taf in a:
                  cl.sendText(taf, (bctxt))
#-----------------------------------------------

            elif "Mugiwara say " in msg.text:
              if msg.from_ in admin:
                  bctxt = msg.text.replace("Mugiwara say ", "")
                  t = cl.getAllContactIds()
                  t = 2
                  while(t):
                    cl.sendText(msg.to, (bctxt))
                    t-=1
#-----------------------------------------------

            elif "Rate " in msg.text:
                tanya = msg.text.replace("Rate ","")
                jawab = ("10% Der","20% Der","15% Der","30% Der","40% Der","50% Der","60% Der","70% Der","80% Der","90% Der","100% Der")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
#------------------------------------------------

            elif "Copy @" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        _name = msg.text.replace("Copy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Succes Copy profile")
                                except Exception as e:
                                    print e
#-----------------------------------------------

            elif msg.text in ["Backup","backup"]:
                if msg.from_ in admin:
                    try:
                       cl.updateDisplayPicture(backup.pictureStatus)
                       cl.updateProfile(backup)
                       cl.sendText(msg.to, "Telah kembali semula")
                    except Exception as e:
                       cl.sendText(msg.to, str(e))
#-----------------------------------------------

            elif msg.text in ["Tak tung"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"Aku belum mandi..Tak tun tuang.. tak tun tuang")
                ki.sendText(msg.to,"Tapi masih cantik juga Tak tun tuang.. tak tun tuang..")
                kk.sendText(msg.to,"Apalagi kalau sudah mandi tak tun tuang..Pasti cantik sekali, ")
                kc.sendText(msg.to,"Kalau orang lain melihat aku tak tun tuang.. Badak aku taba bana Tak tun tuang.. tak tun tuang.")
                ks.sendText(msg.to,"Tapi kalau langsuang diidu tak tun tuang.. Astaghfirullah baunnya:)")
                ko.sendText(msg.to,"Kalau cowok ganteng yang lewat Aku acuah je nyeh")
                ke.sendText(msg.to,"Kalau apak gaek yang lewat Aku aniang je nyeh..")
                ku.sendText(msg.to,"Yang penting indak manggaduah urang tak tun tuang..")
                kb.sendText(msg.to,"Walau acok galak surang Tak tun tuang.. tak tun tuang")
                ka.sendText(msg.to,"Walau sangko urang awak dalang tak tun tuang..")
#-----------------------------------------------
            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                print ("Speed")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s Detik" % (elapsed_time))
#-----------BCKONTCK----------------------------
            elif "Spam @" in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("Spam @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(g.mid,"Ini Adalah Mugiwara")
                       cl.sendText(g.mid,"Ini Adalah Mugiwara")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam") 
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Mugiwara")
                       cl.sendText(g.mid,"Ini Adalah Mugiwara")
                       cl.sendText(g.mid,"Ini Adalah Mugiwara")
                       cl.sendText(g.mid,"Ini Adalah Mugiwara")
                       cl.sendText(msg.to, "Done")
                       print " Spammed !"
#-----------BCKONTK-----------------------------
            elif "Steal " in msg.text:
                if msg. from_ in admin:
                    salsa = msg.text.replace("Steal ","")
                    Manis = cl.getContact(salsa)
                    Imoet = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        cover = cl.channel.getCover(Manis)
                    except:
                        cover = ""
                    cl.sendText(msg.to,"Gambar Foto Profilenya")
                    cl.sendImageWithURL(msg.to,Imoet)
                    if cover == "":
                        cl.sendText(msg.to,"User tidak memiliki cover atau sejenisnya")
                    else:
                        cl.sendText(msg.to,"Gambar Covernya")
                        cl.sendImageWithURL(msg.to,cover)
#------------------------------------------------------------------	
            elif "Steal home @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal home @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#------------------------------------------------------------------
#Restart_Program
            elif msg.text in ["Bot:restart"]:
                cl.sendText(msg.to, "Bot has been restarted")
                restart_program()
                print "@Restart"

            elif "dp @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("dp @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#------------------------------------------------------------------
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact")
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact")
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"nothing👌")
                else:
                    cl.sendText(msg.to,"💀Blacklist user💀")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "🎩" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Cek ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                        kk.kickoutFromGroup(msg.to,[jj])
                        kc.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist emang pantas tuk di usir")
            elif msg.text in ["Clear"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random:" in msg.text:
                if msg.toType == 2:
                    strnum = msg.text.replace("random:","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")	
				
            elif "albumâ†’" in msg.text:
                try:
                    albumtags = msg.text.replace("albumâ†’","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecâ†’" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecâ†’","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass			
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["01","10","20","30","40","50","60","70","80","90","100","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)

                profile2 = mj.getProfile()
                profile2.displayName = wait["cName2"]
                mj.updateProfile(profile2)

                profile3 = k1.getProfile()
                profile3.displayName = wait["cName3"]
                k1.updateProfile(profile3)
            time.sleep(800)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
