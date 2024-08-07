cat <<EOF > AirBnB_clone/tests/test_models/test_base_model.py
#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):
    """Unittests for testing the BaseModel class."""

    def test_initialization(self):
        """Test initialization of a BaseModel instance."""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.created_at, model.updated_at)

    def test_initialization_with_kwargs(self):
        """Test initialization with kwargs."""
        model_id = str(uuid.uuid4())
        now = datetime.now().isoformat()
        model = BaseModel(id=model_id, created_at=now, updated_at=now)
        self.assertEqual(model.id, model_id)
        self.assertEqual(model.created_at.isoformat(), now)
        self.assertEqual(model.updated_at.isoformat(), now)

    def test_save(self):
        """Test the save method."""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

    def test_str(self):
        """Test the __str__ method."""
        model = BaseModel()
        model_str = str(model)
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(model_str, expected_str)

if __name__ == '__main__':
    unittest.main()
EOF

