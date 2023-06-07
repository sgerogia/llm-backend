load('ext://namespace', 'namespace_create', 'namespace_inject')

# --- Variables ---
ns='llm-example'
backend_host='llm-backend'
chatbot_ui_folder='../chatbot-ui'
openai_key=os.environ.get('OPENAI_KEY_BASE64', '')

print("📢 Creating namespace: " + ns)
namespace_create(ns)

print("📢 Applying llm-backend K8s resources")
raw_yaml = read_file('./k8s/llm-backend.yaml')
yaml = str(raw_yaml).format(
    openai_key=openai_key,
)
k8s_yaml(namespace_inject(blob(yaml), ns))

print("📢 Applying chatbot-ui K8s resources")
raw_yaml = read_file(chatbot_ui_folder + '/k8s/chatbot-ui.yaml')
yaml = str(raw_yaml).format(
    api_host='http://' + backend_host + ':8080',
    #api_host='https://api.openai.com',
    default_model='gpt-3.5-turbo',
    system_prompt='You are S.T.R.A.T.O.S, a large language model trained to make the world a better place. Follow the user`s instructions carefully. Respond using markdown.',
    temperature='1',
    log_level='debug',
)
k8s_yaml(namespace_inject(blob(yaml), ns))

print("📢 Building docker images")
docker_build('llm-example/llm-backend', '.', dockerfile='Dockerfile', ignore=['README.md', '.gitignore'])
docker_build('llm-example/chatbot-ui', chatbot_ui_folder, dockerfile=chatbot_ui_folder + '/Dockerfile', ignore=['README.md', '.gitignore'])

print("📢 Launching K8s resources")
k8s_resource('llm-backend', port_forwards='5000:5000')
k8s_resource('chatbot-ui', port_forwards='3000:3000')