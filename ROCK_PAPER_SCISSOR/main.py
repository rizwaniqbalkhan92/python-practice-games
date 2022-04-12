import random;
names_option=['rizwan','rabeeb','abdul hai khan','umer farooq']
# pick_name=input('Enter Other Player Name')
user_name=input('Enter Your Name First : ').lower();
for names in names_option:
    print(names);  
    pick_name=None;  
while pick_name not in names_option:
    pick_name=input('Enter Other Player Name: ').lower();
while True:
    options=['rock','paper','scissors'];
    auto_picker=random.choice(options);
    end_user=None;
    while end_user not in options:
        end_user=input("rock,paper,or scissors ? : "  ).lower();

    if auto_picker == end_user:
        print('{} choose  "{}" '.format(pick_name,auto_picker));
        print('"{}" choose "{}" '.format(user_name,end_user));
        print("Game Tie..!!");
    elif end_user == 'rock':
        if auto_picker == 'paper':
            print('{} choose  "{}" '.format(pick_name,auto_picker));
            print('"{}" choose "{}" '.format(user_name,end_user));
            print("You Loss The Game..!!"); 
        
        if auto_picker == 'scissors':
            print('{} choose  "{}" '.format(pick_name,auto_picker));
            print('"{}" choose "{}" '.format(user_name,end_user));
            print("You Win The Game..!!");
        
    elif end_user == 'paper':
        if auto_picker == 'scissors':
            print('{} choose  "{}" '.format(pick_name,auto_picker));
            print('"{}" choose "{}" '.format(user_name,end_user));
            print("You Loss The Game..!!");
        if auto_picker == 'rock':
            print('{} choose  "{}" '.format(pick_name,auto_picker));
            print('"{}" choose "{}" '.format(user_name,end_user));
            print("You Win The Game..!!");

    again_play=input('Try Again ? Yes or Not: ').lower();
    if again_play != 'yes':
        break;

