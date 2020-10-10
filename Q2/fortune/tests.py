from django.test import TestCase

from fortune.models import Company, FortuneCookie

class CompanyTestCase(TestCase):

    def get_company_with_id(self):
        """Get the company with ID"""
        Company.objects.create(name='RkFortune')
        company_obj = Company.objects.get(id=1)
        self.assertTrue(isinstance(company_obj, Company))


class FortuneCookieTestCase(TestCase):

    def get_fortune_with_name(self):
        """Test fortune data"""
        company_obj = Company.objects.create(name='RkFortune')
        FortuneCookie.objects.create(fortune_option='A miss is as good as a mile.', company_id=company_obj.id)
        cookie_obj = FortuneCookie.objects.get(fortune_option='A miss is as good as a mile.')
        self.assertTrue(isinstance(cookie_obj, FortuneCookie))
