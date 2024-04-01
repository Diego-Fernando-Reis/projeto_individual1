# Projeto de Criptografia de Notas de Alunos

## Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de **criptografar e descriptografar as notas dos alunos**, proporcionando uma forma segura de armazenar e processar informações sensíveis. As notas são organizadas no formato `eX_tX_pX_sX`, onde `X` representa o valor da nota, respectivamente, nos seguintes testes:

- **e**: Entrevista
- **t**: Teste Teórico
- **p**: Teste Prático
- **s**: Avaliação de Soft Skills

Além da criptografia e descriptografia das notas, o sistema também compara as notas descriptografadas com as notas mínimas requeridas em cada tipo de teste, exibindo apenas os alunos que atingem as notas mínimas estabelecidas.

## Funcionalidades

- **Criptografia de Notas**: As notas dos alunos são criptografadas para garantir a privacidade e a segurança das informações.
- **Descriptografia de Notas**: O sistema é capaz de descriptografar as notas para processamento interno e análise dos resultados.
- **Verificação de Notas Mínimas**: Após a descriptografia, as notas são comparadas com os critérios de aprovação mínimos para cada teste, garantindo que apenas os alunos qualificados sejam considerados aprovados.
- **Formatação de Notas**: As notas são organizadas em um formato padronizado (`eX_tX_pX_sX`), facilitando o processamento e a análise dos dados.

## Observações

Uma parte do código foi deixada comentada intencionalmente. Esta seção contempla uma funcionalidade para inserir as notas de maneira dinâmica e já convertê-las para o formato especificado (`eX_tX_pX_sX`). Essa funcionalidade pode ser ativada conforme a necessidade do usuário, oferecendo flexibilidade na manipulação das notas.

## Considerações Finais

Este projeto atende à necessidade de manter as informações dos alunos seguras e acessíveis somente através de processos de **criptografia e descriptografia**. Adicionalmente, a verificação automática das notas mínimas necessárias para aprovação em diferentes tipos de testes otimiza o processo de avaliação, garantindo um padrão de qualificação justo e transparente para todos os alunos.
