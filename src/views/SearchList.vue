<template>
  <v-card
    class="mx-auto"
    max-width="300"
    tile
  >
    <v-text-field
      v-model="word"
      label="input search word"
      outlined
    ></v-text-field>
    <v-divider/>
    <v-list dense>
      <v-subheader>REPORTS</v-subheader>
      <v-list-item-group
        v-model="selectedItem"
        color="primary"
      >
        <v-list-item
          v-for="item in search_items"
          :key="item"
        >
          <v-list-item-content>
            <v-list-item-title v-text="item"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-card>
</template>

<script>

export default {
  name: 'SearchWord',
  components: {
  },
  data () {
    return {
      word: 'a',
      word_list: [
        "ftx29cR82zfXiFz3eCna",
        "WiVnfDkFkLVGZAcEhTXG",
        "B69iaEN5RX3HT6erd44R",
        "DwMtMANsTrMmdhswZRce",
        "XUNWuaJ65JHXjxL8bKZ6",
        "T624Y962LG6QmBMkYYrK",
        "YUaKhFFjDNC5VZNgHKDe",
        "dGFUFxW4WaHMeBztTTGr",
        "936Hmmh4zEsXBjuMFYUz",
        "DGMJgBN5Qz8hbkUuzRRw",
        "WXym559s4LzHCk7x4W96",
        "Z6JtwHg7wecNg85VANPp",
        "kpmZkSafS4CAEySUZfDU",
        "N4pXayAAYrKBVEJdZb5d",
        "C6gLAhj4FdjV3GR7BSPX",
        "W5NEGsJdZsAii9BYMPWB",
        "kfismpQnh9j4Yh7fE7d8",
        "ceTMcDy52wUpSxZbASfm",
        "dDHA8NpVZbaHCrVi2rR3",
        "UpRgKhUMbx3gfnmY8nGH",
        "ihebBepxTiUiVtGPnnE7",
        "nkttWCffPizp9KN7Q5dE",
        "p9TjSc69SXMTKTkWwQ37",
        "hQRSLb9QGkNPjeuyf7SF",
        "59N4Gf9ZPD4ch92xjW7Q",
        "hfMsnzUMfwWKCg7i4tKT",
        "MrSDbCB77uKScAw6Saw8",
        "yY2x2C9K6WkLzFDnarDK",
        "cpHNw8VG6ry7szjmBSpj",
        "Kc6sb5Wgpic3kKwiBEnW",
        "TiHpp5BJFdJGgMyzbtBH",
        "4THB9HnsGZKsQNKJBBcy",
        "B9kEfaYArpGNb5nCnHiE",
        "AXgAp6NyxTQYWzkZUeN6",
        "ZASAQWFSSUm4grasf3WG",
        "dWWTBWQdAAs3mVLsRRAE",
        "aXj64TBtWmiRnEWnTTmf",
        "VdseBysCTW5f7iLgcEnT",
        "Y6u7Pn8gNikjXndJKjkX",
        "3Stm5L5peangwPyaVVmC",
        "dfxNUDLznm5JPVGYSsjT",
        "Qbix52eHJXx34wsYZU8g",
        "h7CGKnMgHbQE6Qs64zVu",
        "Kkwjzy89S8YYddxfcjYV",
        "AgySQLyPeMAxkKgDsnCs",
        "4HFVXksTVBkrJuguT6RK",
        "37xY8MpXrUFN6jBQgpKx",
        "MbMREJLByphEScr9B4up",
        "bUp7FWWEpSjnbVwF5Hnt",
        "7DEzcuPbZp7AXAf6nZR4",
      ]
    }
  },
  mounted(){
    
  },
  //算出プロパティ「computed」はdataに変化があった時に起動します。
  computed:{
      //bestproductsの中に、絞り込まれた商品リストが入ります。
      search_items: function () {
          //ここでitemsリストを絞り込んで返します。
          //this.itemsでこの処理のitemsを呼び出します。
          //その後、filterでリストを絞り込みます。
          //引数としてel(リストの全データ)を渡し、関数内で使えるようにします。
          //elの文字は任意に変更できません。
          return this.word_list.filter(function (el) {
              //データの中の価格が予算より少ないものを選んで絞り込みます。
              //こうして出来上がったリストがbestproductsに格納されます。
                  return el.match(this.word)
          }, this)
      }
  },
  methods:{
  },
}
</script>