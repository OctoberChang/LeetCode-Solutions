#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # input:        barfoothefoobarman
        # l_ptr:        x
        # r_ptr:          x
        # cur_d::{'bar':T}
        # exp_d:{'foo':T
        #        'bar':T}
        #
        ans = []
        if not words or len(words) == 0:
            return ans

        word_len = len(words[0])
        num = len(words)

        # Special cases: s or words are blank or s is less than the combination of words in words
        if (len(s) == 0 or word_len == 0 or len(s) < word_len * num):
            return ans

        expt_count = collections.defaultdict(int)
        for w in words:
            expt_count[w] += 1

        for i in range(len(s) - word_len + 1):
            map_tmp = expt_count.copy()
            j = i
            while j <= len(s) - word_len + 1:
                word_tmp = s[j:j+word_len]

                if word_tmp in map_tmp and map_tmp[word_tmp] > 0:
                    map_tmp[word_tmp] -= 1
                    if map_tmp[word_tmp] == 0:
                        del map_tmp[word_tmp]
                    #print(i, j, map_tmp)
                    if len(map_tmp) == 0:
                        ans.append(i)
                        break
                    j += word_len
                else:
                    break
        # done
        return ans


