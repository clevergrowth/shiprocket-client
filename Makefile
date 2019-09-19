test:
	@(py.test --cov-report term-missing --cov-config .coveragerc --cov=sd_django_utils --color=yes tests/)

serve:
	@(ENV=sample python manage.py migrate && python manage.py runserver)
