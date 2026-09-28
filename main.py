from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class JogoAdivinhacaoApp(App):
    def build(self):
        # Lista com a sequência de frases do roteiro
        self.frases = [
            "Pense em um número de 1 a 10.",
            "Multiplique esse número por 2.",
            "Divida o resultado pelo numero pensado.",
            "Some 2.",
            "Pegue a letra conforme o resultado:\n1=A | 2=B | 3=C | 4=D | 5=E | 6=F | 7=G | e assim por diante...",
            "Pense em um país que começa com a letra obtida.",
            "Pense em um animal que comece com a quinta letra do país."
        ]
        
        self.passo_atual = 0

        # Texto de atenção configurado em caixa alta e vermelho
        sep = "=========================================="
        self.texto_atencao = (
            f"[color=#FF0000]{sep}\n"
            "!!! ATENÇÃO: NA DINAMARCA NÃO TEM MACACO !!!\n"
            f"{sep}[/color]"
        )

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Label para exibir o texto acumulativo
        self.output = Label(
            text="",
            size_hint_y=None,
            markup=True,
            halign='center'
        )
        
        # Ajusta a altura da Label dinamicamente conforme o texto cresce
        self.output.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))

        scroll = ScrollView(size_hint=(1, 0.85))
        scroll.add_widget(self.output)
        layout.add_widget(scroll)

        # Botão interativo
        self.btn = Button(text="OK, prossiga", size_hint_y=None, height=100)
        self.btn.bind(on_press=self.processar_clique)
        layout.add_widget(self.btn)

        # Exibe a primeira frase ao iniciar
        self.mostrar_proxima_frase()

        return layout

    def processar_clique(self, instance):
        # Se o jogo foi concluído e o botão for "Jogar novamente", reinicia o estado
        if self.btn.text == "Jogar novamente":
            self.reiniciar_jogo()
            return

        # Caso contrário, avança para a próxima frase ou exibe o texto final
        if self.passo_atual < len(self.frases):
            self.mostrar_proxima_frase()
        else:
            self.exibir_resultado_final()

    def mostrar_proxima_frase(self):
        nova_frase = self.frases[self.passo_atual]
        
        if self.output.text == "":
            self.output.text = f"[color=#FFFFFF]{nova_frase}[/color]"
        else:
            self.output.text += f"\n\n[color=#FFFFFF]{nova_frase}[/color]"
        
        self.passo_atual += 1

    def exibir_resultado_final(self):
        # Adiciona a mensagem em vermelho no final da exibição
        self.output.text += f"\n\n{self.texto_atencao}"

        # Atualiza o botão para reiniciar o jogo
        self.btn.text = "Jogar novamente"

    def reiniciar_jogo(self):
        # Reseta o estado do jogo
        self.passo_atual = 0
        self.output.text = ""
        self.btn.text = "OK, prossiga"

        # Exibe novamente a primeira instrução
        self.mostrar_proxima_frase()

if __name__ == "__main__":
    JogoAdivinhacaoApp().run()