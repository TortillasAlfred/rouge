import unittest

from rouge.rouge import rouge_l_summary_level, rouge_l_sentence_level
from rouge.tests import rouge_l_sentence_level as _rouge_l_sentence_level
from rouge.tests import summary, reference


class TestRougeL(unittest.TestCase):

    def test_sentence_level(self):
        r_, p_, f_ = _rouge_l_sentence_level(summary, reference, 0.5)
        r, p, f = rouge_l_sentence_level(summary, reference)
        self.assertAlmostEqual(r_, r, places=5)
        self.assertAlmostEqual(p_, p, places=5)
        self.assertAlmostEqual(f_, f, places=5)

    def test_summary_level(self):
        pass