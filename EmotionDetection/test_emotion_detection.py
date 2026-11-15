"""Unit tests for emotion_detector."""
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Tests for the dominant emotion."""

    def test_emotions(self):
        """Check each sample statement maps to the expected emotion."""
        cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]
        for text, expected in cases:
            self.assertEqual(emotion_detector(text)["dominant_emotion"], expected)


if __name__ == "__main__":
    unittest.main()
