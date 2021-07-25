<template>
  <div>
    <div style="height: 500px; border: solid 1px #ddd; margin: 50px">
      <c-grid :data="records"
              :frozen-col-count="1">
        <c-grid-column field="id"
                       width= "50">
          ID
        </c-grid-column>
        <c-grid-radio-column field="selected"
                             width="50">
          選択
        </c-grid-radio-column>
        <c-grid-button-column caption="削除"
                              width="50"
                              @click="onDeleted">
          削除
        </c-grid-button-column>
        <c-grid-check-column field="checked"
                             width="70">
          フラグ
        </c-grid-check-column>
        <c-grid-column-group caption="データ">
          <c-grid-input-column field="data1"
                               width="20%"
                               min-width="150">
            データ1
          </c-grid-input-column>
          <c-grid-input-column field="data2"
                               width= "20%"
                               min-width="150">
            データ2
          </c-grid-input-column>
        </c-grid-column-group>
        <c-grid-menu-column field="type"
                            :options="[{label: '種別1', value: 1},
                                       {label: '種別2', value: 2},
                                       {label: '種別3', value: 3}]">
                種別
        </c-grid-menu-column>
        <c-grid-link-column href="link"
                            :icon="getLinkIcon">
                詳細
        </c-grid-link-column>
        <c-grid-percent-complete-bar-column field="percent"
                                            :max="100"
                                            :min="0">
                割合
        </c-grid-percent-complete-bar-column>
        <c-grid-icon-column field="iconNum"
                            icon-class-name="material-icons"
                            icon-content="grade">
                アイコン
        </c-grid-icon-column>
      </c-grid>
    </div>
    <div class="grid-sample"></div>
  </div>
</template>
<script>
import * as cGridAll from 'vue-cheetah-grid'
export default {
    name: 'service',
    components: {
        ...cGridAll
    },
    mounted() {
        this.setRecord()
    },
    data () {
        return {
            records: []
        }
    },
    methods: {
        /**
         * 削除ボタン押下イベント
         *
         * @param {object} rec 行データ
         * @return {void}
         **/
        onDeleted(rec) {
            const vm = this
            vm.records.splice(vm.records.indexOf(rec), 1);
        },
        /**
         * 一覧に表示するデータを作成する
         *
         * @return {void}
         **/
        setRecord () {
            const vm = this
            for (let i=0; i < 1000; i++) {
                vm.records.push({
                    selected: false,
                    checked: false,
                    id: i+1,
                    data1: `サンプル1-${i+1}`,
                    data2: `サンプル2-${i+1}`,
                    type: Math.floor(Math.random() * 3) + 1,
                    link: "https://future-architect.github.io/cheetah-grid/documents/api/vue/components/CGridLinkColumn.html",
                    iconNum: 1,
                    percent: Math.round(Math.random() * 100)
                })
            }
        },
        /**
         * c-grid-link-columnに表示するアイコンを取得する
         *
         * @return {object} アイコン情報
         **/
        getLinkIcon () {
            return {
                className: 'material-icons',
                content: 'input'
            }
        }
    }
}
</script>