from courses.models import Course

def copy_courses(qs=Course.objects.all()):
	if qs.count() < 100:
		for i in qs:
			user 		= i.user
			title 		= i.title
			image 		= i.image
			category 	= i.category
			secondary 	= i.secondary.all()
			description = i.description
			price		= i.price
			new_obj = Course.objects.create(
				user = user,
				title = title,
				image = image,
				category = category,
				description = description,
				price = price,
			)
			# new_obj.secondary = secondary
			for cat in secondary:
				new_obj.secondary.add(cat)
			new_obj.save()
		qs2 = Course.objects.all()
		if qs2.count() <= 100:
			return copy_courses(qs=qs2)
	return qs.count()

copy_courses()