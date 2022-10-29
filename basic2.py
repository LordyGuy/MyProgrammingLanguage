   res.register_advancement()
    self.advance()

    condition = res.register(self.statement())
    condition = res.register(self.expr())
    if res.error: return res

    if not self.current_tok.matches(TT_KEYWORD, 'THEN'):
      def if_expr_cases(self, case_keyword):
