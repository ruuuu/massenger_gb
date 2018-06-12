from Response import RResponse
import pytest
from pytest import raises


class Test_client: # модульные тесты


  def test_create_presence(self):
      r = RResponse()
      message = r.create_presence(account_name="Guest")
      assert message['action'] == "hhlohyo" #presence