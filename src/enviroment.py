from envparse import env

env.read_envfile()

proxy = env('PROXY')
input_url = env('INPUT_URL')
output_file = env('OUTPUT_FILE')