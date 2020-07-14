<template>
    <div class="hello">
        <markdown-it-vue-light class="md-body" :content="content" :options="options"/>
    </div>
</template>

<script>
import MarkdownItVueLight from 'markdown-it-vue/dist/markdown-it-vue-light.umd.min.js'
import 'markdown-it-vue/dist/markdown-it-vue-light.css'
    export default {
        components: {
        MarkdownItVueLight
        },
        name:'',
        data(){
            return{
                name: "test",
                content:'``` js\n' +
                    'var foo = function (bar) {\n' +
                    '  return bar++;\n' +
                    '};\n' +
                    '\n' +
                    'console.log(foo(5));\n' +
                    '```',
                options:{
                    highlight: function (str, lang) {
                        // 此处判断是否有添加代码语言
                        if (lang && hljs.getLanguage(lang)) {
                          try {
                            // 得到经过highlight.js之后的html代码
                            const preCode = hljs.highlight(lang, str, true).value
                            // 以换行进行分割
                            const lines = preCode.split(/\n/).slice(0, -1)
                            // 添加自定义行号
                            let html = lines.map((item, index) => {
                              return '<li><span class="line-num" data-line="' + (index + 1) + '"></span>' + item + '</li>'
                            }).join('')
                            html = '<ol>' + html + '</ol>'
                            // 添加代码语言
                            if (lines.length) {
                              html += '<b class="name">' + lang + '</b>'
                            }
                            return '<pre class="hljs"><code>' +
                              html +
                              '</code></pre>'
                          } catch (__) {}
                        }
                        // 未添加代码语言，此处与上面同理
                        const preCode = md.utils.escapeHtml(str)
                        const lines = preCode.split(/\n/).slice(0, -1)
                        let html = lines.map((item, index) => {
                          return '<li><span class="line-num" data-line="' + (index + 1) + '"></span>' + item + '</li>'
                        }).join('')
                        html = '<ol>' + html + '</ol>'
                        return '<pre class="hljs"><code>' +
                          html +
                          '</code></pre>'
                      }

                }

            }
        },
        methods:{

        },
        created(){

        }

    }
</script>

<style scoped>

</style>