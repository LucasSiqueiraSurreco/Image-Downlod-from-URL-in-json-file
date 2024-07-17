import requests
import json
import os

def download_image(url, file_path):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'pt-BR,pt;q=0.7',
        'cache-control': 'max-age=0',
        'dnt': '1',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Linux',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }

    try:
        # Verifica se o arquivo já existe
        if os.path.exists(file_path):
            print(f'Arquivo {file_path} já existe. Pulando download.')
            return

        response = requests.get(url, headers=headers, stream=True)
        if response.status_code == 200:
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)
            print(f'Download de {url} concluído.')
        else:
            print(f'Erro ao baixar {url}. Status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Erro ao baixar {url}. Exceção: {e}')
    except Exception as e:
        print(f'Erro inesperado ao baixar {url}. Exceção: {e}')

def download_images_from_json(json_file):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
            if 'products' in data:
                for product in data['products']:
                    if 'imgUrl' in product:
                        url = product['imgUrl']
                        filename = url.split('/')[-1]
                        file_path = f'imagens_downloads/{filename}'
                        download_image(url, file_path)
                    else:
                        print(f'URL inválida no JSON: {product}')
            else:
                print('JSON não contém a chave "products".')
    except FileNotFoundError:
        print(f'Arquivo JSON não encontrado: {json_file}')
    except json.JSONDecodeError as e:
        print(f'Erro ao decodificar JSON em {json_file}. Exceção: {e}')
    except Exception as e:
        print(f'Erro inesperado ao processar o arquivo JSON {json_file}. Exceção: {e}')

# Exemplo de uso
json_file = 'imagens.json'
download_images_from_json(json_file)
