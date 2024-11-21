# test_poker.py

import unittest
from unittest.mock import patch
import random
from collections import Counter
from Poker_v2 import (
    reset_deck,
    draw_card,
    draw_hand,
    set_rank,
    set_order,
    royal_flush,
    determine_combination
)

class TestPoker(unittest.TestCase):

    def test_reset_deck(self):
        deck = reset_deck()
        self.assertEqual(len(deck), 52)
        suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
        card_types = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 
                      'Jack', 'Queen', 'King', 'Ace']
        expected_deck = [(suit, card) for suit in suits for card in card_types]
        self.assertListEqual(sorted(deck), sorted(expected_deck))

    @patch('random.choice')
    def test_draw_card(self, mock_choice):
        mock_choice.return_value = ('Hearts', 'Ace')
        deck = reset_deck()
        drawn_card = draw_card(deck)
        self.assertEqual(drawn_card, ('Hearts', 'Ace'))
        self.assertNotIn(('Hearts', 'Ace'), deck)
        self.assertEqual(len(deck), 51)

    @patch('random.choice')
    def test_draw_hand(self, mock_choice):
        mock_choice.side_effect = [('Clubs', '2'), ('Spades', '3'), 
                                   ('Hearts', '4'), ('Diamonds', '5'), 
                                   ('Clubs', '6')]
        deck = reset_deck()
        hand = draw_hand(deck, 5)
        expected_hand = [('Clubs', '2'), ('Spades', '3'), 
                        ('Hearts', '4'), ('Diamonds', '5'), 
                        ('Clubs', '6')]
        self.assertListEqual(hand, expected_hand)
        self.assertEqual(len(deck), 47)

    def test_set_rank(self):
        self.assertEqual(set_rank('2'), 0)
        self.assertEqual(set_rank('10'), 8)
        self.assertEqual(set_rank('Jack'), 9)
        self.assertEqual(set_rank('Queen'), 10)
        self.assertEqual(set_rank('King'), 11)
        self.assertEqual(set_rank('Ace'), 12)
        with self.assertRaises(KeyError):
            set_rank('Joker')

    def test_set_order(self):
        hand = [('Hearts', '5'), ('Clubs', '2'), ('Spades', 'Ace'), 
                ('Diamonds', '10'), ('Hearts', 'King')]
        ordered_hand = set_order(hand)
        expected_order = [('Clubs', '2'), ('Hearts', '5'), 
                         ('Diamonds', '10'), ('Hearts', 'King'), 
                         ('Spades', 'Ace')]
        self.assertListEqual(ordered_hand, expected_order)

    def test_royal_flush_true(self):
        hand = [('Hearts', '10'), ('Hearts', 'Jack'), ('Hearts', 'Queen'), 
                ('Hearts', 'King'), ('Hearts', 'Ace')]
        self.assertTrue(royal_flush(hand))

    def test_royal_flush_false_different_suit(self):
        hand = [('Hearts', '10'), ('Hearts', 'Jack'), ('Hearts', 'Queen'), 
                ('Hearts', 'King'), ('Spades', 'Ace')]
        self.assertFalse(royal_flush(hand))

    def test_royal_flush_false_missing_card(self):
        hand = [('Hearts', '10'), ('Hearts', 'Jack'), ('Hearts', 'Queen'), 
                ('Hearts', 'King'), ('Hearts', '9')]
        self.assertFalse(royal_flush(hand))

    def test_determine_combination_royal_flush(self):
        hand = [('Hearts', '10'), ('Hearts', 'Jack'), ('Hearts', 'Queen'), 
                ('Hearts', 'King'), ('Hearts', 'Ace')]
        combination = determine_combination(hand, 5)
        self.assertEqual(combination, "Royal Flush")

    def test_determine_combination_straight_flush(self):
        hand = [('Clubs', '6'), ('Clubs', '7'), ('Clubs', '8'), 
                ('Clubs', '9'), ('Clubs', '10')]
        combination = determine_combination(hand, 5)
        self.assertEqual(combination, "Straight Flush")

    def test_determine_combination_four_of_a_kind(self):
        hand = [('Hearts', '9'), ('Clubs', '9'), ('Spades', '9'), 
                ('Diamonds', '9'), ('Hearts', 'King')]
        combination = determine_combination(hand, 5)
        self.assertEqual(combination, "Four of a Kind")

    def test_determine_combination_full_house(self):
        hand = [('Hearts', '8'), ('Clubs', '8'), ('Spades', '8'), 
                ('Diamonds', 'King'), ('Hearts', 'King')]
        combination = determine_combination(hand, 5)
        self.assertEqual(combination, "Full House")

    def test_determine_combination_flush(self):
        hand = [('Hearts', '2'), ('Hearts', '5'), ('Hearts', '9'), 
                ('Hearts', 'Jack'), ('Hearts', 'King')]
        combination = determine_combination(hand, 5)
        self.assertEqual(combination, "Flush")

    def test_determine_combination_straight(self):
        hand = [('Clubs', '4'), ('Hearts', '5'), ('Spades', '6'), 
                ('Diamonds', '7'), ('Hearts', '8')]
        combination = determine_combination(hand, 5)
        self.assertEqual(combination, "Straight")

    def test_determine_combination_three_of_a_kind(self):
        hand = [('Hearts', '3'), ('Clubs', '3'), ('Spades', '3'), 
                ('Diamonds', '7'), ('Hearts', 'King')]
        combination = determine_combination(hand, 5)
        self.assertEqual(combination, "Three of a Kind")

    def test_determine_combination_two_pair(self):
        hand = [('Hearts', '4'), ('Clubs', '4'), ('Spades', '9'), 
                ('Diamonds', '9'), ('Hearts', 'King')]
        combination = determine_combination(hand, 5)
        self.assertEqual(combination, "Two Pair")

    def test_determine_combination_one_pair(self):
        hand = [('Hearts', '5'), ('Clubs', '5'), ('Spades', '9'), 
                ('Diamonds', 'Jack'), ('Hearts', 'King')]
        combination = determine_combination(hand, 5)
        self.assertEqual(combination, "One Pair")

    def test_determine_combination_high_card(self):
        hand = [('Hearts', '2'), ('Clubs', '5'), ('Spades', '9'), 
                ('Diamonds', 'Jack'), ('Hearts', 'King')]
        combination = determine_combination(hand, 5)
        self.assertEqual(combination, "High Card")

if __name__ == '__main__':
    unittest.main()
