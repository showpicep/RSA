from PyQt5.QtWidgets import QMainWindow
from ui_files.RSA import Ui_RSA
from PyQt5.QtWidgets import QMessageBox
import datetime
from modules.pows import tryParseInt, powm
from modules.rsa_func import Get_prime_dig, Get_n, Get_func, Get_e, Get_d


def Dec(func):
    def Wrapper(*args, **kwargs):
        if len(args[0].ui.p_field.toPlainText()) != 0:
            if len(args[0].ui.input_field.toPlainText()) != 0:
                return func(args[0])
            else:
                UIWindow.ShowError('Вы не ввели текст!')
        else:
            UIWindow.ShowError('Вы не сгенерировали данные!')
    return Wrapper


class UIWindow(QMainWindow):
    """ Класс графического интерфейса для основной формы """

    def __init__(self) -> None:
        """ Иницаилизация """
        super(UIWindow, self).__init__()
        self.ui = Ui_RSA()
        self.ui.setupUi(self)
        self.add_functions_for_buttons()
        self.setFixedSize(1000, 690)

    def add_functions_for_buttons(self) -> None:
        """ Метод для добавления функций для кнопок """
        self.ui.gen_btn.clicked.connect(self.GenerateNum)
        self.ui.encode_btn.clicked.connect(self.Encode)
        self.ui.decode_btn.clicked.connect(self.Decode)

    @Dec
    def Decode(self):
        if len(self.ui.encoded_field.toPlainText()) != 0:
            d, n = int(self.ui.d_field.toPlainText()), int(self.ui.n_field.toPlainText())
            crypt_mess = self.ui.encoded_field.toPlainText()
            crypt_mess = crypt_mess.split()
            decrypted_m = ''

            for i in crypt_mess:
                lett = powm(int(i), d, n) % 1114111
                decrypted_m += chr(lett)

            self.ui.decoded_field.setPlainText(str(decrypted_m))
        else:
            self.ShowError('Нечего расшифровывать!')

    @Dec
    def Encode(self):
        e, n = int(self.ui.e_field.toPlainText()), int(self.ui.n_field.toPlainText())
        message = self.ui.input_field.toPlainText()
        crypt_mess = ''
        #message = message.split()

        for item in message:
            lett = str(powm(ord(item), e, n)) + ' '
            crypt_mess += str(lett)

        self.ui.encoded_field.setPlainText(crypt_mess)

    def GenerateNum(self):
        """ Метод для генерации чисeл"""
        num_bits, flag = tryParseInt(self.ui.nbits_field.toPlainText())
        test_count = 10

        if flag:
            self.ui.p_field.setPlainText(str(Get_prime_dig(num_bits)))
            self.ui.q_field.setPlainText(str(Get_prime_dig(num_bits)))
            self.ui.n_field.setPlainText(str(Get_n(self.ui.p_field.toPlainText(), self.ui.q_field.toPlainText())))
            self.ui.fn_field.setPlainText(str(Get_func(self.ui.p_field.toPlainText(), self.ui.q_field.toPlainText())))
            self.ui.e_field.setPlainText(str(Get_e(num_bits)))
            self.ui.d_field.setPlainText(str(Get_d(self.ui.fn_field.toPlainText(), self.ui.e_field.toPlainText())))
        else:
            self.ShowError('Некорректный ввод кол-ва битов!')

    @staticmethod
    def ShowError(error_text: str) -> None:
        """Метод для отображения ошибки"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(error_text)
        msg.setWindowTitle("Attantion")
        msg.exec_()
