from django.test import TestCase, Client


class GetDriver(TestCase):
    def setUp(self):

        self.client = Client()

    def test_driver_list_endpoint(self):
        # Test verilerini oluşturabilirsiniz
        test_request_data = {
            "offset": 0,
            "limit": 10,
        }

        # Endpoint'e GET isteği gönder
        response = self.client.get('/driver_list/', test_request_data)

        # Status kodunu kontrol et
        self.assertEqual(response.status_code, 200)

        # Response içeriğini kontrol et (örneğin, JSON formatında bir response bekliyorsanız)
        response_data = response.json()
        self.assertIn("items", response_data)
        self.assertIn("total", response_data)
        self.assertIn("offset", response_data)
        self.assertIn("limit", response_data)
