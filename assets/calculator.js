(function () {
  'use strict';
  function calculate(price, days, percent, extra) {
    if (![price, days, percent, extra].every(Number.isFinite) || price < 0 || !Number.isSafeInteger(days) || days <= 0 || percent <= 0 || percent > 100 || extra < 0) {
      throw new RangeError('请填写非负金额、正整数天数和大于0且不超过100的支付比例。');
    }
    const total = price * percent / 100 + extra;
    if (!Number.isFinite(total) || !Number.isFinite(total / days * 30)) throw new RangeError('金额过大，请检查输入。');
    return {total, daily: total / days, per30: total / days * 30};
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = {calculate};
  if (typeof document === 'undefined') return;
  const form = document.querySelector('#cost-calculator');
  if (!form) return;
  form.hidden = false;
  const output = document.querySelector('#cost-result');
  form.addEventListener('input', function () {
    output.textContent = '输入已变更，请重新点击计算。';
  });
  const money = n => n.toLocaleString('zh-CN', {minimumFractionDigits:2, maximumFractionDigits:2});
  form.addEventListener('submit', function (event) {
    event.preventDefault();
    try {
      const results = ['a', 'b'].map(prefix => {
        const values = ['price','days','percent','extra'].map(key => {
          const input = form.elements[prefix + '-' + key];
          if (!input.value.trim()) throw new RangeError('请填写两个方案的全部数值。');
          return Number(input.value);
        });
        return calculate(...values);
      });
      const rows = results.map((r,i)=>'方案'+(i===0?'A':'B')+'：总支出 '+money(r.total)+'；每天 '+money(r.daily)+'；每30天 '+money(r.per30)+'。');
      const difference = results[0].per30 - results[1].per30;
      rows.push(Math.abs(difference)<0.005 ? '按30天折算，两者成本相同。' : '按30天折算，方案'+(difference<0?'A':'B')+'较低，差额为 '+money(Math.abs(difference))+'。');
      rows.push('金额单位与输入一致。只有币种、账号权限与使用条件一致时才可比较；折算成本不是实际月费，也不构成购买建议。');
      output.textContent = rows.join('\n');
    } catch (error) {
      output.textContent = error.message;
    }
  });
}());
