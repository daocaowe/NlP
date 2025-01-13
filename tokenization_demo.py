# 导入必要的库
import jieba
import nltk
from nltk.tokenize import word_tokenize

def chinese_tokenization_demo():
    """中文分词示例"""
    print("\n=== 中文分词示例 ===")
    
    # 示例1：基础分词
    text = "我喜欢在北京大学学习自然语言处理"
    words = jieba.cut(text)
    print(f"基础分词：{'| '.join(words)}")
    
    # 示例2：全模式分词
    words_full = jieba.cut(text, cut_all=True)
    print(f"全模式分词：{'| '.join(words_full)}")
    
    # 示例3：搜索引擎模式
    words_search = jieba.cut_for_search(text)
    print(f"搜索引擎模式：{'| '.join(words_search)}")
    
    # 示例4：添加自定义词典
    jieba.add_word('自然语言处理')
    words_custom = jieba.cut(text)
    print(f"添加自定义词后：{'| '.join(words_custom)}")

def english_tokenization_demo():
    """英文分词示例"""
    print("\n=== 英文分词示例 ===")
    
    # 下载必要的数据
    nltk.download('punkt')
    
    # 示例1：基础分词
    text = "NLTK is a powerful library for natural language processing!"
    tokens = word_tokenize(text)
    print(f"基础分词：{tokens}")

def advanced_tokenization_demo():
    """高级分词示例"""
    print("\n=== 高级分词示例 ===")
    
    # 示例1：词性标注
    import jieba.posseg as pseg
    text = "小明在北京大学读计算机专业"
    words = pseg.cut(text)
    print("词性标注：")
    for word, flag in words:
        print(f'{word}({flag})', end=' ')
    print("\n")
    
    # 示例2：处理特殊文本
    text2 = "我来自北京邮电大学计算机学院，最近在研究AI技术"
    jieba.add_word('北京邮电大学')
    jieba.add_word('计算机学院')
    words = jieba.cut(text2)
    print(f"处理特殊文本：{'| '.join(words)}")

def main():
    """主函数"""
    print("分词示例程序开始运行...")
    
    # 运行中文分词示例
    chinese_tokenization_demo()
    
    # 运行英文分词示例
    english_tokenization_demo()
    
    # 运行高级分词示例
    advanced_tokenization_demo()

if __name__ == "__main__":
    main() 