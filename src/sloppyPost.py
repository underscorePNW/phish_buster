

# global varible declaration
# word list is declared globally to reduce re-reading
# during iteration
with open('../util/dictionary.json') as file_object:
    file_object = open('../util/dictionary.json')
    json_object = json.load(file_object)
site_settings = {'url': 'https://linstagramphotographycontests.pythonanywhere.com/login', 'username_field': 'username',
                 'password_field': 'password'}


def generate_combo_list(length):
    def generate_fake_email():
        output_string = ''
        number_of_names = random.randrange(1, 3, 1)
        include_period = random.choice([True, False])
        include_number = random.choice([True, False])
        if include_number:
            # addition to numbers for emails, start value is to simulate unavailable emails
            # stop value is set to simulate year of birth aswell
            include_number = random.randrange(500, 2000, 1)
        print(number_of_names)

        for i in range(number_of_names):
            output_string += random.choice(json_object)
            if include_period:
                output_string += '.'
        if include_number > 0:
            output_string += str(include_number)
        return output_string + str(random.choice(['@gmail.com', '@yahoo.com', '@apple.com', '@aol.com']))

    def generate_password():
        pw_length = random.randrange(10, 16, 1)
        pw_string = ''
        for i in range(pw_length):
            pw_string += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        return pw_string

    user_pass_dict = {}
    for i in range(length):
        user_pass_dict[generate_fake_email()] = generate_password()
    return user_pass_dict


# def spoof_phisher(username, password):
def spoof_phisher(user_pass_combo_tuple):
    import time
    _int_time = time.time()

    username = user_pass_combo_tuple[0]
    password = user_pass_combo_tuple[1]
    try:
        data_dict = {site_settings['username_field']: username,
                     site_settings['password_field']: password}

        print(data_dict.items())
        response_obj = req.post(site_settings['url'], data=data_dict)
        _final_time = time.time()
        print('Status Code : '+str(response_obj.status_code))
        print('Requesting '+str(10/(_final_time - _int_time))+' post requests per second')

        return response_obj.content
    except Exception as e:
        print(e)


def initiate_spam_campaign(max_workers, spam_entries):
    import time
    inital_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        result = executor.map(spoof_phisher, generate_combo_list(spam_entries).items())
    completed_time = time.time()
    print('Spam Signups Completed!')
    print('Process took: '+str(completed_time-inital_time)+ ' seconds for'+str(spam_entries)+' entries!')
    print('average request rate: ' + str(spam_entries / (completed_time-inital_time)) + ' per second')
    return result



initiate_spam_campaign(50, 10000)
# rename_me = spoof_phisher(url, request_method, username, password,username_field,password_field)

# print(rename_me)

