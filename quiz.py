from datetime import datetime, timedelta
from typing import List



class Event(object):
    user_id: int = None # a number that uniquely identifies a user in our system
    event_date: datetime = None # the exact date and time that an event was completed at
    action_name: str = None # one of the following: "incorrect_answer", "correct_answer", "word_learnt"

    def __init__(self, user_id, event_date, action_name):
        self.user_id = user_id
        self.event_date = event_date
        self.action_name = action_name
        

def get_30_day_leaderboard_user_ids(engagement_events: List[Event]) -> List[int]:
    """""
    Build a leaderboard that ranks users from fastest learning to slowest learning based on how many
    "words_learnt" events they achieved during the previous 30 days.
    Only users with at least 15 actions taken in the last 30 days are considered for the leaderboard.
    :return: a list of user ids, ordered from most words learnt to least words learnt

    """
    period = datetime.now() - timedelta(days=30)
    users = []
    leaderboard = []
    action_counts = []
    

    for event in engagement_events:
        if event.user_id not in users:
            users.append(event.user_id)
        
    for user in users:
        user_actions = 0
        for event in engagement_events:
            if event.user_id == user and event.event_date>=period:
                user_actions += 1
        
        if user_actions>=15:
            leaderboard.append(user)
            
                     
    for user in leaderboard:
        user_events = 0
        for event in engagement_events:
            if  event.user_id == user and event.action_name =='word_learnt' and event.event_date>=period:
                user_events += 1
        action_counts.append(user_events)
        
    
    
    leaderboard_dict = {leaderboard[i]: action_counts[i] for i in range(0, len(leaderboard))}
    leaderboard_dict = dict(sorted(leaderboard_dict.items(), key=lambda item: item[1],reverse=True))
    
    result = list(leaderboard_dict.keys())
    return result
    

 
yesterday = datetime.now() - timedelta(days=1)
events = [Event(1, yesterday, "word_learnt"), Event(1, yesterday, "word_learnt"), Event(1, yesterday, "word_learnt"),
          Event(1, yesterday, "word_learnt"),
          Event(2, yesterday, "word_learnt"), Event(3, yesterday, "word_learnt"),
          Event(3, yesterday, "word_learnt"),
          Event(4, yesterday, "word_learnt")]

for i in range(16):
    events.append(Event(1, yesterday, "correct_answer"))
    events.append(Event(2, yesterday, "correct_answer"))
    events.append(Event(3, yesterday, "correct_answer"))


leaderboard = get_30_day_leaderboard_user_ids(events)
assert (leaderboard == [1,3,2])
