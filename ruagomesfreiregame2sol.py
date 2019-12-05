import random
import math

# LearningAgent to implement
# no knowledeg about the environment can be used
# the code should work even with another environment
class LearningAgent:
        def __init__(self,nS,nA):
                self.nS = nS
                self.nA = nA

                self.q_table = [ [ float("-inf") for i in range(nA) ] for j in range(nS) ]
                self.nExplored = [ [0 for i in range(nA) ] for j in range(nS) ]

                self.alfa = 0.20
                self.gama = 0.90
                self.thresh = .99
                self.maxExplorations = 500

        def selectactiontolearn(self,st,aa):
                max = self.q_table[st][0]
                action = random.randint(0, len(aa)-1)

                if random.random() > self.thresh:
                    for index in range(0, len(aa)):
                        if self.q_table[st][index] > max:
                            max = self.q_table[st][index]
                            action = index
                        elif self.q_table[st][index] == max:
                             if random.randint(0,1) == 1:
                                 action = index

                else:
                    if self.thresh < 0.1:
                       self.thresh = 0.1;

                    aux = self.lessExplored(st, aa)
                    if aux != []:
                       action = aux[random.randint(0, len(aux)-1)]
                       if self.nExplored[st][action] > self.maxExplorations:
                           aux.remove(self.nExplored[st][action])
                           if aux != []:
                               action = aux[random.randint(0, len(aux)-1)]
                           else:
                               action = random.randint(0, len(aa)-1)
                    self.thresh = self.thresh * 0.993

                self.nExplored[st][action] += 1
                return action

        def selectactiontoexecute(self,st,aa):
                max = self.q_table[st][0]
                action = 0
                
                for index in range(0, len(aa)):
                    if self.q_table[st][index] > max:
                        max = self.q_table[st][index]
                        action = index
                    elif self.q_table[st][index] == max:
                        if random.randint(0,1) == 1:
                            action = index

                return action

        def learn(self,ost,nst,a,r):
                max = 0

                aux = float("-inf")
                for i in self.q_table[nst]:
                    if i > aux:
                        aux = i

                if math.isinf(aux):
                    max = 0
                else:
                    max = aux

                if not math.isinf(self.q_table[ost][a]):
                    self.q_table[ost][a] = self.q_table[ost][a] + self.alfa * (r + self.gama * max - self.q_table[ost][a])
                else:
                    self.q_table[ost][a] = r + self.gama * max
                return

        def lessExplored(self, st, aa):
            res = self.nExplored[st][0]
            result = 0
            aux = []

            for i in range(0, len(aa)):
                if self.nExplored[st][i] < res:
                    res = self.nExplored[st][i]
                    result = i

            for i in range(0, len(aa)):
                if self.nExplored[st][i] == res and self.nExplored[st][i] <= self.maxExplorations:
                    aux.append(i)

            return aux
