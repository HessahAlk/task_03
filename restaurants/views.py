from django.shortcuts import render

def welcome(request):
	return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
	restaurants=[
		{
			'name':'Bella',
			'type': 'Italian'
		},
		{
			'name':'Zara',
			'type':'Indian'
		},
		{
			'name':'Bazza',
			'type':'Kuwaiti'
		},
	]
	context = {
		'my_list': restaurants,
	    }
	return render(request, 'list.html', context)


def restaurant_detail(request):
	restaurantsdet={
	'name':'Bella', 'type':'Italian'
	}

	context = {'my_object': restaurantsdet,

	}
	return render(request, 'detail.html', context)