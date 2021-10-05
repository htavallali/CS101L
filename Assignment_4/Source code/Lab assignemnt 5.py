########################################################################
##
## CS 101 Lab
## 
## Hedieh Tavallali
## httnm@umsystem.edu
##
## PROBLEM : Describe the problem

##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      ## OTHER COMMENTS:
##      
##
########################################################################

#import modules needed

import

def play_again_returns_True(self) 
user_input = ["YeS"]
with patch('sys.stdout', new_callable=StringIO) as es:
with patch('builtins.input', side_effect=user_input):
results = lab05.play_again()
self.assertTrue(results, "When input is yes the function should return True")    

    return True
def play_again_returns_False_with_N_or_NO(self):

user_input = ["nO"]
with patch('sys.stdout', new_callable=StringIO) as es:
with patch('builtins.input', side_effect=user_input):
results = lab05.play_again()
self.assertFalse(results, "When input is No play_again should return False")

     
def get_wager_returns_wager_amount(self)
user_input = ["30"]
with patch('sys.stdout', new_callable=StringIO) as es:
with patch('builtins.input', side_effect=user_input):
results = lab05.get_wager(200)
self.assertEqual(30, results, "getWager should return 30 when the user enters 30")


def test_get_wager_returns_wager_amount_after_negative(self):

user_input = ["-5", "45"]
with patch('sys.stdout', new_callable=StringIO) as es:
with patch('builtins.input', side_effect=user_input):
results = lab05.get_wager(200)
self.assertEqual(45, results, "getWager should return 45 when the user enters -5, 30")

def test_get_wager_returns_wager_amount_after_negative(self):

user_input = ["-5", "45"]
with patch('sys.stdout', new_callable=StringIO) as es:
with patch('builtins.input', side_effect=user_input):
results = lab05.get_wager(200)
self.assertEqual(45, results, "getWager should return 45 when the user enters -5, 30")
l = es

def test_get_wager_returns_wager_amount_after_too_high_value(self):

user_input = ["105", "22"]
with patch('sys.stdout', new_callable=StringIO) as es:
with patch('builtins.input', side_effect=user_input):
results = lab05.get_wager(30)
self.assertEqual(22, results, "getWager should return 22 when the user enters 105, 22, and the bank is less than 105")
l = es


    return 1            

def get_slot_results(self) 

results = lab05.get_slot_results()
self.assertIsInstance(results, tuple, "get_slot_results should return a tuple")
self.assertEqual(3, len(results), "get_slot_results shoudl return 3 items")
self.assertIsInstance(results[0], int, "Item at index 0 was not an integer")
self.assertIsInstance(results[1], int, "Item at index 1 was not an integer")
self.assertIsInstance(results[2], int, "Item at index 2 was not an integer")

    return 1, 2, 3

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''

    return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''

    return 0

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    return wager * -1     


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while True:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()
