import hashlib
from models import Client, Server
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import uuid

@csrf_exempt
def login(request):
	print 'blarg'
	if request.method == 'POST':
		print 'passed check 1'
		if request.POST.__contains__('user') and request.POST.__contains__('sessionid'):
			print 'passed if'
			hash = hashlib.md5(request.POST.__getitem__('sessionid')).hexdigest()
			print 'got hash'
			client = Client(user=request.POST.__getitem__('user'), sessionid=str(request.POST.__getitem__('sessionid')), md5=hash)
			print 'made client'
			
			print 'saved user'
			client.save()
			print 'saved client'
			return HttpResponse(hash)
			
		else:
			return HttpResponse('Invalid Request')
	if request.method == 'GET':
		return HttpResponse('ERROR')
		

@csrf_exempt		
def addserver(request):
	if request.method == 'POST':
		if request.POST.__contains__('name') and request.POST.__contains__('ip_address'):
			id = hashlib.md5(str(uuid.uuid4())).hexdigest()
			print 'uuid made'
			if request.POST.__contains__('password'):
				phash = hashlib.sha224(request.POST.__getitem__('password') + hashlib.md5(request.POST.__getitem__('password')).hexdigest())
				password = True
			else:
				phash = 'NULL'
				password = False
			print 'pssword solved'
			server = Server(name = request.POST.__getitem__('name'), uuid = id, ip_address = request.POST.__getitem__('ip_address'), has_pass = password, password = phash)
			print 'server amde'
			return HttpResponse(id)
			
		else:
			return HttpResponse('Invalid Request')
@csrf_exempt			
def validate(request):
	if request.method == 'POST':
		print 'checked'
		if request.POST.__contains__('id'):
			print 'checked 2'
			try:
				print 'trying'
				Client.objects.get(md5=request.POST.__getitem__('id'))
				print 'tried'
			except DoesNotExist:
				print 'excepted'
				return HttpResponse('Invalid Client')
				
			else:
				return HttpResponse('Valid Client')
			
	
			
