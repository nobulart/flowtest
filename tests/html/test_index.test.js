describe('Data Table', () => {
test('loads CSV into table', async () => {
document.body.innerHTML = '<table id="data-table"></table>';
global.fetch = jest.fn(() => Promise.resolve({ text: () => Promise.resolve('1,2,3\n4,5,6') }));
await import('../../index.html');
const table = document.getElementById('data-table');
expect(table.querySelectorAll('tr').length).toBe(2);
});
});