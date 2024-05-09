#anotar as coisa que quero ter no meu chat
#nome : amor chat
#botao de iniciar chat
    #abrir um pop up / modal
        #bem vindo ao amorzap
        #amor escreva seu nome aqui
            #botao entrar no chat
                #carregar o chat

#chat 
    #caixa de escrita a mensagem e outro de enviar

# usaremos o flet que é um framework(conjunto de ferramentas usadas no codigo todo)
#cada framework tem suas regras são usados no coigo todo
#frameworks mais famosos django, flet, flask

import flet as ft

def main(pagina):

    
        
    chat = ft.Column()
    
    def enviar_mensagem_tunel(mensagem):
        #sempre que um usuario enviar uma mensagem eu quero que todos usuarios recebam ela
        #print(mensagem)

        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar(texto):

        pagina.pubsub.send_all(f"{nome_usuario.value} : {digitar_chat.value}")
        #adiciona a mensagem no chat
        
        #limpa o campo mensagem
        digitar_chat.value = ""
        #pagina updade
        pagina.update()


    def digitando(digitando):
        pagina.pubsub.send_all(f"{nome_usuario.value} está digitando")   

    digitar_chat = ft.TextField(label="Digite sua mensagem...", on_submit=enviar, on_change=digitando)
    enviar_chat = ft.ElevatedButton("Enviar", on_click=enviar)
    linha_enviar = ft.Row([digitar_chat, enviar_chat])
        
    def entrar_chat(evento):
        #fechar o pop
        popup.open = False
        #tirar o botão iniciar chat
        pagina.remove(botao_iniciar)
        #tirar o titulo
        pagina.remove(texto_inicial)
        #criar o chat
        pagina.add(chat)
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
        #campo digitar mensagem 
        #criar o botão de enviar
        pagina.add(linha_enviar)
        pagina.update()



    texto_inicial = ft.Text("amor zap", font_family="Arial", text_align= "center")


    textopopup = ft.Text("Bem vindo ao Amorzap")
    nome_usuario = ft.TextField(label="Escreva seu nome", on_submit=entrar_chat) #Textfiel é um campo digitavel e label(rotulo) é o texto do campo
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=textopopup,
        content=nome_usuario,
        actions=[botao_entrar]#sempre passar em uma lista os botoes do pop up
    )
    
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        #sempre que editar a pagina depois de carregada com pagina.update

    
    
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup, color="red")
    pagina.add(texto_inicial)
    pagina.add(botao_iniciar)


ft.app(target=main, view=ft.WEB_BROWSER) #chama a função principal
