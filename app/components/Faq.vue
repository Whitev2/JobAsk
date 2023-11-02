<template>
  <section class="contact-form-one faq-page">
    <div class="container">
      <!-- Контейнер выравнивает по ширине и по центру -->
      <div class="container_form" id="faq">

        <!-- content содержит содержимое формы -->
        <div class="content">


          <!-- Правая колонка: сама форма -->
          <div class="right-side">

            <!-- Заголовок для формы -->
            <div class="topic-text">Записаться на бесплатную консультацию</div>

            <!-- Какой-то дополнительный текст -->
            <p>
              Если у вас остались вопросы или вы желаете получить услугу - заполните форму ниже и наш менеджер свяжется
              с вами
            </p>

            <!-- Форма обратной связи -->
            <div class="form">
              <!-- Каждый input для выравнивания вкладываем в блок input-box -->
              <div class="input-box">
                <input v-model="name" type="text" placeholder="Ваше имя"/>
              </div>
              <div class="input-box">
                <input v-model="email" type="text" placeholder="Введите email"/>
                <p class="item__error" >
                  {{ emailError }}
                </p>
              </div>
              <div class="input-box">
                <input v-model="phone" type="text" placeholder="Введите телефон"/>
              </div>
              <div class="input-box message-box">
                <textarea v-model="question" placeholder="Интересующая вас услуга или вопрос"></textarea>
              </div>
              <div class="button">
                <input type="submit" @click="modalValidation"/>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div><!-- /.container -->
  </section>
</template>

<script>
export default {
  name: "Faq",
  data() {
    return {
      emailError: '',
      name: "",
      email: "",
      phone: "",
      question: "",
    }
  },
  methods: {
    async modalValidation() {
      this.emailValidation()
      if (this.emailError.length === 0) {
        //тут делаем отправку на сервер
        console.log(this.name)
        console.log(this.email)
      }
    },
    regexValidation(re, str) {
      return re.test(str)
    },
    emailValidation() {
      if (!this.regexValidation(/^([\wА-я.-]+)@([\w.-]+)\.([A-z]{1,10})$/, this.email)) {
        this.emailError = 'Недопустимый email'
        return false
      }
      this.emailError = ''
      return true
    },
  },
}
</script>

function()

<style scoped>

*,
*::after,
*::before {
  box-sizing: inherit;
}

/* При расчете размеров инпутов учитываем внутренние отступы и границы */
input,
textarea {
  box-sizing: border-box;
}

/* В body устанавливаем шрифт, ширину и высоту, а также фон */
body {
  font-family: "Roboto", sans-serif;
  font-size: 16px;
  line-height: 1.2;
  width: 100%;
  min-height: 100vh;
  background: linear-gradient(45deg, #fff1eb, #ace0f9);
  display: flex;
  justify-content: center; /* чтобы контейнер */
  align-items: center; /* был по центру */
}

/* Ограничиваем контейнер по ширине 1000px */
.container_form {
  width: 100%;
  max-width: 1000px;
  padding: 0 20px;
}

/* Стили самой формы */
.content {
  display: flex; /* делаем колонки в ряд */
  align-items: center; /* выравниваем по центру */
  justify-content: space-between; /* колонки растянутся на всю ширину */
  background: #e0e0e0;
  padding: 40px;
  border-radius: 5px;
  box-shadow: 4px 4px 8px 0 rgba(34, 60, 80, 0.2);
}

/* Стили правой колонки */
.right-side {
  width: 100%; /* занимает 75% общей ширины */
  margin-left: 75px;
}


/* Общие стили для иконок */
.details i {
  font-size: 25px; /* задаем размер */
  color: #3e2093; /* задаем цвет */
  margin-bottom: 10px;
}

/* Заголовок правой колонки */
.topic-text {
  font-size: 23px;
  font-weight: 600;
  color: #3e2093;
  margin-bottom: 10px;
}

/* Текст правой колонки */
.right-side p {
  margin-bottom: 20px;
}

/* Контейнер для input'ов формы */
.input-box {
  height: 50px; /* по сути задаем высоту input'а */
  width: 100%; /* ширина на всю ширину правой колонки (с учетом padding) */
  margin-bottom: 40px; /* отступаем снизу 20px */
}

/* Стили для input и textarea (поле сообщение) */
.input-box input,
.input-box textarea {
  height: 100%; /* растягиваем на всю высоту контейнера 50px */
  width: 100%; /* растягиваем на всю ширину */
  border: none; /* убираем внешние края */
  border-radius: 5px; /* скругляем края */
  background: #f0f1f8; /* задаем цвет фона */
  padding: 0 20px; /* отступ справа и слева 20px */
}

/* Отдельно стилизуем поле сообщение */
.input-box textarea {
  resize: none; /* чтобы нельзя было менять высоту */
  padding: 20px;
  font-family: "Roboto", sans-serif;
}

/* Это контейнер для поля сообщение */
.message-box {
  min-height: 110px; /* минимальная высота 110px */
}

/* Стили для контейнера кнопки */
.button {
  display: inline-block; /* делаем блочно-строчный элемент */
}

/* Стили для самой кнопки */
.button input[type="button"] {
  color: #969494;
  font-size: 18px;
  background: #3e2093;
  outline: none;
  border: none;
  padding: 10px 20px;
  border-radius: 7px;
  transition: 0.2s; /* чтобы плавно менялся цвет при наведении (:hover) */
}

/* Меняем цвет фона при наведении на кнопку */
.button input[type="button"]:hover {
  background: rgb(0, 0, 207);
}

/* Меняем стили при ширине экрана меньше 800px */
@media (max-width: 800px) {
  /* Теперь форма (правая колонка) будет сверху, а элементы (левая колонка) снизу */
  .content {
    height: 100%;
    flex-direction: column-reverse; /* располагаем в колонку и реверсивно */
  }

  /* Внутри левой колонки внутренние элементы располагаем в ряд */
  .left-side {
    margin-top: 50px;
    flex-direction: row; /* располагаем элементы (адрес, телефон, email) в ряд */
    width: 100%; /* левая колонка на всю ширину */
    justify-content: center;
    flex-wrap: wrap; /* перенос элементов, если не хватит места */
  }

  .details {
    margin-right: 20px;
  }

  .details:last-child {
    margin-right: 0;
  }

  /* Убираем разделительную линию */
  .left-side::before {
    display: none;
  }

  /* Правая колонка теперь на всю ширину и не имеет отступа слева */
  .right-side {
    width: 100%;
    margin-left: 0;
  }
}

.item__error {
  color: #b02500;
}

</style>
