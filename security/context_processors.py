#coding: utf8

def user_active(request):
	data = {}
	if request.user.is_authenticated():
		data['uanombre'] = request.user.get_full_name()
	else:
		data['uanombre'] = "Usiario anonimo"

	return data		